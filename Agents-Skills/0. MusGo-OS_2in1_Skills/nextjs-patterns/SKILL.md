---
name: nextjs-patterns
description: "Master Next.js patterns (App Router, server components, server actions, data fetching, middleware, route handlers, static generation, metadata) to build optimized, scalable apps."
metadata:
  tags: "autonomous-agents, web-development, next-js, app-router, server-components, server-actions, data-fetching, middleware"
  source: "https://skilldb.dev/skills/autonomous-agent-skills/nextjs-patterns"
  pack: "autonomous-agent-skills"
  category: "Autonomous Agents"
---

# Next.js Patterns

## When to use this skill
Use when the user says things like:
- "Explain Next.js patterns and when to use them"
- "Give me Next.js App Router best practices"
- "Explain server components vs client components"
- "Show how to implement server actions"
- "Provide routing, middleware, and metadata patterns"


You are an autonomous agent that builds and modifies Next.js applications. Your role is to leverage Next.js features correctly, choosing the right rendering strategy for each page and understanding the boundary between server and client code.

## Philosophy

Next.js is a full-stack React framework. Its power comes from making the right rendering decisions per page and per component. Default to server components and server-side rendering. Move to the client only when interactivity demands it. The framework handles the complexity of hydration, streaming, and caching — your job is to give it the right signals.

## Techniques

### App Router vs Pages Router
- New projects should use the App Router (`app/` directory). It is the current architecture.
- In existing Pages Router projects (`pages/` directory), follow the existing patterns unless migrating.
- Do not mix routing paradigms. If the project uses App Router, do not create files in `pages/` (except `pages/api` during migration).
- Understand the difference: App Router uses React Server Components by default, Pages Router uses `getServerSideProps` / `getStaticProps`.

### Server Components
- Components in the App Router are server components by default. They run on the server and send HTML to the client.
- Server components can directly access databases, file systems, and environment variables without exposing them to the client.
- Server components cannot use hooks (`useState`, `useEffect`), browser APIs, or event handlers.
- Keep server components as the default. Only add `'use client'` when the component needs interactivity.
- Push `'use client'` boundaries as deep as possible. A page can be a server component that renders a small client component for an interactive widget.

### Server Actions
- Define server actions with `'use server'` directive at the top of the function or file.
- Use server actions for form submissions, data mutations, and any operation that modifies server state.
- Server actions can be passed directly to form `action` attributes for progressive enhancement.
- Validate all inputs in server actions — they are public API endpoints despite looking like function calls.
- Call `revalidatePath()` or `revalidateTag()` after mutations to update cached data.

### Data Fetching Patterns
- In server components, use `async/await` directly: `const data = await db.query(...)`.
- Use `fetch` with Next.js caching options: `fetch(url, { next: { revalidate: 3600 } })` for time-based revalidation.
- Use `cache()` from React to deduplicate data fetching across components in the same render.
- For client-side data fetching, use TanStack Query or SWR, not raw `useEffect` + `fetch`.
- Avoid waterfalls: fetch data in parallel with `Promise.all` when requests are independent.

### Middleware
- Use `middleware.ts` at the project root for request-level logic: authentication checks, redirects, header modification.
- Keep middleware fast — it runs on every matching request. Do not perform database queries or heavy computation.
- Use the `matcher` config to limit which routes trigger middleware.
- Middleware runs on the Edge runtime. Only use Edge-compatible APIs.

### Route Handlers
- Create API endpoints in `app/api/[route]/route.ts` with exported `GET`, `POST`, `PUT`, `DELETE` functions.
- Route handlers replace Pages Router API routes. They support streaming, Web API Request/Response objects.
- Use route handlers for webhooks, third-party API proxying, and endpoints consumed by external clients.
- For internal data mutations, prefer server actions over route handlers.

### Dynamic Routes and Routing
- Use folder-based routing: `app/blog/[slug]/page.tsx` for dynamic segments.
- Use catch-all routes `[...slug]` for flexible path matching.
- Generate static params with `generateStaticParams()` for static generation of dynamic routes.
- Use route groups `(group)` to organize routes without affecting the URL structure.
- Use parallel routes `@slot` and intercepting routes `(.)` for complex UI patterns like modals.

### Static Generation vs Server Rendering
- Default to static generation for pages with content that does not change per request.
- Use `generateStaticParams` to pre-render dynamic routes at build time.
- Use `dynamic = 'force-dynamic'` or `revalidate = 0` for pages that must be server-rendered on every request.
- Use ISR (Incremental Static Regeneration) with `revalidate` for pages that change periodically.
- Understand the rendering: static pages are cached at the CDN, dynamic pages are rendered per request.

### Image Optimization
- Use `next/image` for all images. It handles lazy loading, responsive sizing, and format optimization.
- Set explicit `width` and `height` to prevent layout shift, or use `fill` with a sized container.
- Configure `remotePatterns` in `next.config.js` for external image domains.
- Use `priority` on above-the-fold images to preload them.

### Metadata Management
- Export `metadata` objects or `generateMetadata` functions from page and layout files.
- Include `title`, `description`, and `openGraph` properties for SEO and social sharing.
- Use `generateMetadata` when metadata depends on dynamic data (e.g., blog post title from database).
- Define default metadata in the root layout and override in child pages.

## Best Practices
- Use TypeScript throughout. Next.js has excellent built-in TypeScript support.
- Colocate loading, error, and not-found states with their routes: `loading.tsx`, `error.tsx`, `not-found.tsx`.
- Use environment variables with `NEXT_PUBLIC_` prefix only for client-side values. Keep secrets server-only.
- Configure `next.config.js` explicitly — understand what each option does before setting it.
- Use the Next.js cache effectively, but understand when to opt out.

## Anti-Patterns
- Adding `'use client'` to every component, negating the benefits of server components.
- Using `useEffect` for data fetching in server-component-capable routes.
- Performing heavy computation in middleware instead of in route handlers or server actions.
- Ignoring input validation in server actions because they feel like local function calls.
- Using `next/image` without specifying dimensions, causing layout shift.
- Placing all state in a single client-side provider at the root, forcing the entire app to be client-rendered.
- Fetching the same data in multiple server components without using React's `cache()` for deduplication.
- Hardcoding URLs instead of using `next/link` for client-side navigation.