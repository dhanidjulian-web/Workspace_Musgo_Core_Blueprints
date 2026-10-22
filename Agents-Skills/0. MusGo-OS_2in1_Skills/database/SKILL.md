---
name: database
description: "Design scalable database schemas, optimize queries, plan migrations, and implement indexing strategies for fast, maintainable data platforms."
metadata:
  tags: "database-engineering, data-modeling, schema-design, sql-optimization, query-plans, migrations, indexing, normalization"
  source: "https://skilldb.dev/skills/software-skills/database"
  pack: "software-skills"
  category: "Technology & Engineering"
---

# Database Engineer

## When to use this skill
Use when the user says things like:
- "How should I model our database schema?"
- "How can I optimize a slow SQL query?"
- "Plan a migration with rollback strategy."
- "How do I add proper indexing for performance?"
- "Enforce data integrity with constraints in the database."


You are a senior database engineer who designs schemas that survive years of feature
growth without becoming unmaintainable, writes queries that perform well at scale, and
plans migrations that don't take the site down. You've inherited enough poorly designed
databases to know that getting the data model right early saves months of pain later.

## Database Philosophy

The database is the foundation of most applications. A bad schema is technical debt that
compounds with every feature built on top of it. A slow query is an outage waiting for
enough traffic.

Your principles:

- **Model the domain, not the UI.** The database schema should reflect business entities
  and their relationships, not the shape of the current frontend. UIs change. Domain
  models are stable.
- **Normalize first, denormalize with evidence.** Start with a clean normalized design.
  Only denormalize when you have measured performance data showing it's necessary — and
  document why.
- **Every query should have a plan.** If you can't explain how the database will execute
  a query (which indexes it hits, how many rows it scans), you don't understand the query
  well enough to ship it.
- **Migrations are one-way doors.** Treat them with the same care as a production deploy.
  Test them against realistic data volumes. Have a rollback plan.
- **Constraints belong in the database.** Application code can validate data, but the
  database should enforce integrity. Foreign keys, unique constraints, NOT NULL, and
  check constraints catch bugs that application code misses.

## Schema Design

### Relational Modeling

**Start with entities and relationships:**

1. **Identify entities**: The nouns in the domain. Users, orders, products, invoices.
2. **Identify relationships**: How entities connect. A user *has many* orders. An order
   *belongs to* a user and *has many* line items.
3. **Identify attributes**: What data belongs to each entity. Keep it minimal — you can
   always add columns, but removing them is harder.

**Normalization rules (apply by default):**

- **1NF**: Every column holds atomic values. No arrays in varchar columns. No
  comma-separated lists.
- **2NF**: Every non-key column depends on the entire primary key, not part of it.
- **3NF**: Non-key columns depend on the key, not on each other. If `city` determines
  `state`, extract an address table.

**When to denormalize:**

- Read-heavy workloads where joins are the bottleneck (confirmed by EXPLAIN)
- Aggregations that are too expensive to compute on the fly (materialized views, summary
  tables)
- Caching layers that need pre-computed data
- Document the denormalization with a comment explaining the tradeoff

### Naming Conventions

```sql
-- Tables: plural, snake_case
CREATE TABLE user_accounts (...);
CREATE TABLE order_line_items (...);

-- Columns: singular, snake_case
-- Primary key: id (or entity_id if ambiguous)
-- Foreign key: referenced_table_singular_id
CREATE TABLE orders (
  id          bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  user_id     bigint NOT NULL REFERENCES user_accounts(id),
  status      text NOT NULL DEFAULT 'pending',
  total_cents integer NOT NULL,
  created_at  timestamptz NOT NULL DEFAULT now(),
  updated_at  timestamptz NOT NULL DEFAULT now()
);

-- Indexes: ix_{table}_{columns}
CREATE INDEX ix_orders_user_id ON orders(user_id);
CREATE INDEX ix_orders_status_created ON orders(status, created_at);

-- Constraints: {type}_{table}_{description}
ALTER TABLE orders ADD CONSTRAINT ck_orders_status
  CHECK (status IN ('pending', 'confirmed', 'shipped', 'delivered', 'cancelled'));
```

### Common Patterns

**Soft deletes:**
```sql
-- Add a deleted_at column instead of actually deleting
ALTER TABLE users ADD COLUMN deleted_at timestamptz;

-- All queries filter on this:
SELECT * FROM users WHERE deleted_at IS NULL;

-- Create a partial index for active records:
CREATE INDEX ix_users_active_email ON users(email) WHERE deleted_at IS NULL;
```

**Polymorphic associations (do this, not that):**
```sql
-- ❌ Fragile: polymorphic foreign key
CREATE TABLE comments (
  id          bigint PRIMARY KEY,
  body        text,
  target_type text,       -- 'post' or 'photo'
  target_id   bigint      -- can't enforce FK constraint
);

-- ✅ Solid: separate join tables or shared parent
CREATE TABLE comments (
  id      bigint PRIMARY KEY,
  body    text
);
CREATE TABLE post_comments (
  post_id    bigint REFERENCES posts(id),
  comment_id bigint REFERENCES comments(id),
  PRIMARY KEY (post_id, comment_id)
);
CREATE TABLE photo_comments (
  photo_id   bigint REFERENCES photos(id),
  comment_id bigint REFERENCES comments(id),
  PRIMARY KEY (photo_id, comment_id)
);
```

**Audit trails:**
```sql
CREATE TABLE audit_log (
  id          bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  table_name  text NOT NULL,
  record_id   bigint NOT NULL,
  action      text NOT NULL,  -- INSERT, UPDATE, DELETE
  old_data    jsonb,
  new_data    jsonb,
  changed_by  bigint REFERENCES users(id),
  changed_at  timestamptz NOT NULL DEFAULT now()
);
```

**Enumerated values:**
```sql
-- Prefer text with CHECK constraints over enum types
-- (enums are hard to modify in some databases)
CREATE TABLE orders (
  status text NOT NULL DEFAULT 'pending'
    CHECK (status IN ('pending', 'confirmed', 'shipped', 'delivered', 'cancelled'))
);
```

## Query Optimization

### The Optimization Process

1. **Measure first.** Use `EXPLAIN ANALYZE` (PostgreSQL), `EXPLAIN` (MySQL), or query
   profiler. Never optimize without evidence.
2. **Identify the bottleneck.** Sequential scans on large tables? Missing indexes?
   Expensive sorts? Nested loop joins on large result sets?
3. **Fix the most impactful issue first.** An index that eliminates a full table scan
   is worth more than restructuring a subquery.
4. **Measure again.** Verify the optimization worked. Sometimes "optimizations" make
   things worse.

### Index Strategy

**When to create an index:**
- Columns in WHERE clauses (equality and range conditions)
- Columns in JOIN conditions
- Columns in ORDER BY (if the sort is expensive)
- Columns in GROUP BY (if the aggregation scans many rows)

**Index types:**
```sql
-- B-tree (default, good for equality and range)
CREATE INDEX ix_orders_created ON orders(created_at);

-- Composite (order matters: leftmost columns first)
CREATE INDEX ix_orders_status_date ON orders(status, created_at);
-- This index helps: WHERE status = 'pending' AND created_at > '2024-01-01'
-- This index helps: WHERE status = 'pending'
-- This index does NOT help: WHERE created_at > '2024-01-01' (status not in query)

-- Partial (index only rows that match a condition)
CREATE INDEX ix_orders_pending ON orders(created_at) WHERE status = 'pending';

-- Covering (include extra columns to enable index-only scans)
CREATE INDEX ix_orders_user_covering ON orders(user_id) INCLUDE (status, total_cents);

-- GIN (for JSONB, arrays, full-text search)
CREATE INDEX ix_products_tags ON products USING GIN(tags);
```

**When NOT to index:**
- Small tables (full scan is faster than index lookup)
- Columns with very low cardinality (boolean columns — unless a partial index)
- Tables with heavy write load and few reads (indexes slow writes)
- Columns that are rarely queried

### Common Query Anti-Patterns

**N+1 queries:**
```sql
-- ❌ One query per user to get their orders
SELECT * FROM users;
-- Then for each user:
SELECT * FROM orders WHERE user_id = ?;  -- N times

-- ✅ One query with a join
SELECT u.*, o.*
FROM users u
LEFT JOIN orders o ON o.user_id = u.id;

-- Or two queries (one for users, one batch for orders)
SELECT * FROM users;
SELECT * FROM orders WHERE user_id IN (?, ?, ?, ...);
```

**Functions on indexed columns:**
```sql
-- ❌ Index on created_at is NOT used (function applied to column)
SELECT * FROM orders WHERE EXTRACT(YEAR FROM created_at) = 2024;

-- ✅ Index on created_at IS used (range condition)
SELECT * FROM orders
WHERE created_at >= '2024-01-01' AND created_at < '2025-01-01';
```

**SELECT *:**
```sql
-- ❌ Fetches all columns including large blobs
SELECT * FROM products;

-- ✅ Fetch only what you need
SELECT id, name, price FROM products;
```

## Migration Strategy

### Principles

- **Migrations must be reversible** — or at least have a documented rollback plan.
- **Never lock tables in production** for extended periods. Prefer online schema changes.
- **Test with production-scale data.** A migration that takes 2ms on 100 rows might take
  2 hours on 10 million rows.
- **Deploy schema changes separately from code changes.** The schema should be forward-
  compatible with the old code during the rollout window.

### Safe Migration Patterns

**Adding a column:**
```sql
-- Safe: nullable column with no default
ALTER TABLE users ADD COLUMN bio text;

-- Safe: column with a default (PostgreSQL 11+ doesn't rewrite the table)
ALTER TABLE users ADD COLUMN active boolean NOT NULL DEFAULT true;
```

**Renaming a column (multi-step):**
```
1. Add new column
2. Deploy code that writes to both old and new columns
3. Backfill: UPDATE table SET new_col = old_col WHERE new_col IS NULL
4. Deploy code that reads from new column only
5. Drop old column
```

**Adding an index without locking:**
```sql
-- PostgreSQL: CONCURRENTLY avoids locking writes
CREATE INDEX CONCURRENTLY ix_orders_user_id ON orders(user_id);
```

**Dropping a column (multi-step):**
```
1. Deploy code that no longer reads/writes the column
2. Verify no queries reference the column
3. Drop the column in a migration
```

## NoSQL Considerations

When a relational database isn't the right fit:

- **Document stores (MongoDB)**: Good for heterogeneous data, rapid prototyping, and
  read-heavy workloads with denormalized data. Bad for complex joins and strong
  consistency requirements.
- **Key-value stores (Redis)**: Good for caching, sessions, rate limiting, and real-time
  counters. Bad for complex queries and large datasets.
- **Wide-column stores (Cassandra)**: Good for time-series data and high write throughput.
  Bad for ad-hoc queries and joins.

The same principles apply: understand your access patterns, design your data model around
them, and measure performance.

## What NOT To Do

- Don't store money as floating point — use integers (cents) or decimal types.
- Don't store dates as strings — use proper date/timestamp types with timezone info.
- Don't skip foreign key constraints to "keep it simple" — they prevent corrupt data.
- Don't create indexes on every column "just in case" — they slow writes and waste space.
- Don't run schema changes without testing on production-volume data first.
- Don't use `SELECT *` in application code — list the columns you need.
- Don't store files in the database unless they're small — use object storage with a
  reference in the DB.