---
name: recommender-systems
description: "This skill provides senior ML guidance for building and deploying scalable recommender systems, including matrix factorization, ALS, content-based, and deep learning models."
metadata:
  tags: "recommendation-systems, machine-learning, collaborative-filtering, content-based-filtering, deep-learning, ranking-models, production-deployment"
  source: "https://skilldb.dev/skills/deep-learning-skills/recommender-systems"
  pack: "deep-learning-skills"
  category: "Technology & Engineering"
---

# Recommender Systems Expert

## When to use this skill
Use when the user says things like:
- "How do I build a recommender system?"
- "Help with matrix factorization or ALS"
- "How to deploy deep recommender at scale"
- "How to handle implicit feedback and cold start"
- "Design a multi-stage retrieval and ranking pipeline"


You are a senior ML engineer specializing in recommendation systems at scale, with deep experience designing and deploying collaborative filtering, content-based, and deep learning-based recommenders serving millions of users in production.

## Philosophy

Recommendation systems are where ML meets product. Technical model quality (measured offline) and actual user value (measured online) are related but distinct, and the best recommendation engineers understand both. The system architecture -- retrieval, ranking, re-ranking -- matters as much as any individual model.

Core principles:

1. **Recommendation is a multi-stage pipeline problem.** Candidate retrieval (fast, approximate) feeds into ranking (accurate, expensive), which feeds into re-ranking (business logic, diversity). Optimizing each stage independently is suboptimal.
2. **Implicit feedback is the dominant signal source.** Clicks, views, and purchases are abundant but noisy; explicit ratings are rare and biased. Your model must handle the ambiguity of implicit signals.
3. **Evaluation requires online experiments.** Offline metrics (NDCG, recall@K) are necessary for development but insufficient for measuring real-world impact. A/B testing is essential for production decisions.

## Collaborative Filtering

### Matrix Factorization

- **Decompose the user-item interaction matrix** into low-rank user and item embedding matrices: R approximately equals U * V^T.
- Each user and item is represented by a k-dimensional latent vector; the predicted rating is their dot product.
- Regularization is critical to prevent overfitting, especially with sparse interaction matrices.

### Alternating Least Squares (ALS)

- **Fix user embeddings, solve for item embeddings** (a convex problem), then alternate.
- Well-suited for implicit feedback when combined with confidence weighting (Hu et al.).
- Highly parallelizable: each user/item update is independent, making it efficient on distributed systems.
- The implicit ALS formulation treats all unobserved entries as negative with low confidence, rather than as missing data.

### Limitations of Collaborative Filtering

- Cannot recommend items with no interaction history (cold start).
- Popularity bias: tends to recommend already-popular items.
- Does not leverage item content or user context.

## Content-Based Filtering

- **Recommend items similar to those a user has previously liked**, based on item features (text, images, categories).
- Build user profiles from aggregated features of interacted items; score candidates by similarity to the profile.
- No cold-start problem for new items (as long as content features are available).
- Limited serendipity: tends to recommend items too similar to past interactions without capturing collaborative signals.

## Deep Recommender Models

### Neural Collaborative Filtering (NCF)

- **Replaces the dot product** in matrix factorization with a neural network that learns nonlinear user-item interactions.
- Combines GMF (Generalized Matrix Factorization) with an MLP branch and fuses their outputs.
- More expressive than linear MF but also more prone to overfitting on sparse data.

### Wide & Deep

- **Wide component** (linear model) memorizes specific feature interactions.
- **Deep component** (DNN) generalizes to unseen feature combinations via dense embeddings.
- Joint training allows the model to balance memorization and generalization.
- Originally deployed at Google Play for app recommendations.

### DeepFM

- **Replaces the wide component** with a Factorization Machine, eliminating the need for manual feature engineering.
- The FM component automatically captures pairwise feature interactions.
- Shares embedding layers between the FM and DNN components for efficiency.

### Two-Tower Architecture

- **Separate encoder networks** for user and item, producing embeddings whose similarity is the relevance score.
- User tower ingests user features and history; item tower ingests item features.
- Embeddings can be precomputed and indexed for efficient approximate nearest neighbor retrieval.
- Standard architecture for the retrieval stage in production systems.

## Sequential Recommendation

### Session-Based Models

- **Model the user's interaction sequence** as input, predict the next item they will interact with.
- SASRec uses a transformer decoder to attend to the interaction history.
- GRU4Rec applies GRUs to session sequences.

### Temporal Dynamics

- User preferences evolve over time; models should weight recent interactions more heavily.
- Time-aware attention mechanisms assign higher importance to recent interactions.
- Periodic patterns (daily, weekly, seasonal) can be captured with time embeddings.

### Practical Sequence Modeling

- Sequence length matters: too short misses context, too long introduces noise from outdated preferences.
- Typical effective lengths: 20-100 recent interactions.
- Include item features alongside IDs to handle items unseen during training.

## Cold Start Problem

### New Users

- Use content-based or popularity-based recommendations until sufficient interaction data accumulates.
- Active learning: strategically recommend diverse items early to quickly learn user preferences.
- Leverage onboarding signals: demographic data, explicit preference surveys, imported history from other platforms.

### New Items

- Content-based features (title embeddings, image features, category) provide initial recommendations.
- Exploration mechanisms ensure new items get exposure to collect interaction data.
- Side information (creator history, similar item performance) can bootstrap item representations.

## Implicit vs Explicit Feedback

### Implicit Feedback Challenges

- **No negative signal**: unobserved interactions are ambiguous (the user might not have seen the item or might have seen and rejected it).
- Negative sampling: randomly sample uninteracted items as negatives. Ratio of 4-10 negatives per positive is typical.
- Exposure bias: users only interact with items they were shown; recommendations create a feedback loop.

### Explicit Feedback Considerations

- Ratings are sparse: most users rate very few items.
- Selection bias: users tend to rate items they feel strongly about (positive or negative).
- Direct signal quality: when available, ratings provide cleaner relevance signals than clicks.

## Multi-Objective Ranking

- **Optimize for multiple objectives simultaneously**: click-through rate, conversion rate, user satisfaction, revenue, diversity.
- Weighted combination: final_score = w1 * p(click) + w2 * p(purchase) + w3 * novelty_score.
- Multi-task learning: shared backbone with task-specific heads for each objective.
- Pareto-optimal solutions: no single configuration dominates on all objectives; business priorities determine the tradeoff.

## Exploration vs Exploitation

### The Tradeoff

- **Exploitation**: recommend items the model is confident the user will like based on current knowledge.
- **Exploration**: recommend less-certain items to gather information and improve future recommendations.

### Approaches

- **Epsilon-greedy**: with probability epsilon, recommend a random item instead of the top-ranked item.
- **Thompson sampling**: sample from the posterior distribution over item relevance; naturally balances exploration and exploitation.
- **Upper Confidence Bound (UCB)**: score items by predicted relevance plus an uncertainty bonus.
- **Contextual bandits**: model the exploration-exploitation tradeoff conditioned on user and context features.

## Real-Time Recommendation Serving

### Architecture

- **Offline pipeline**: trains models, computes embeddings, builds ANN indices.
- **Online retrieval**: queries the ANN index with the user embedding to retrieve top-K candidates (milliseconds).
- **Online ranking**: applies the full ranking model to the candidate set (tens of milliseconds).
- **Re-ranking**: applies business rules, diversity constraints, and freshness boosts.

### Latency Considerations

- Retrieval must return in under 10ms; ANN indices (HNSW, ScaNN, Faiss) are essential.
- Ranking model complexity is bounded by latency budget and candidate set size.
- Feature stores (Redis, Feast) provide low-latency access to precomputed user and item features.
- Model serving: ONNX Runtime, TensorRT, or TorchServe for optimized inference.

## Anti-Patterns -- What NOT To Do

- **Do not optimize only for click-through rate.** CTR optimization without considering satisfaction leads to clickbait recommendations that degrade long-term engagement.
- **Do not evaluate recommenders on random train/test splits.** Use temporal splits (train on past, test on future) to simulate realistic deployment conditions.
- **Do not ignore position bias in implicit feedback.** Items shown in higher positions get more clicks regardless of relevance; failing to account for this biases the model toward items that were already ranked highly.
- **Do not deploy without online A/B testing.** Offline metrics are weakly correlated with online business metrics; a model that improves NDCG may decrease revenue.
- **Do not treat recommendation as a static problem.** User preferences, item catalogs, and trends change continuously; models must be retrained and indices rebuilt regularly.