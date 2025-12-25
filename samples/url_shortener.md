# System Design: URL Shortener

## Traffic
1M Requests per day

---

## High-Level Architecture
- API Gateway
- URL Shortener Service
- Database
- Cache
- Load Balancer

---

## Data Flow
1. Client sends long URL
2. API Gateway routes request
3. Short URL generated and stored
4. Short URL returned
5. Redirect handled via GET

---

## API Design
### POST /shorten
- Input: long_url
- Output: short_url

### GET /{short_url}
- Redirects to original URL

### GET /stats/{short_url}
- Returns analytics

---

## Database Schema
### shortened_urls
- id
- long_url
- short_url
- created_at

### analytics
- id
- short_url
- clicks
- views

---

## Caching & Scaling
- Redis for hot URLs
- Horizontal scaling behind load balancer
- Auto-scaling based on traffic

---

## Bottlenecks & Trade-offs
- DB write pressure
- Cache invalidation complexity
- Cost vs performance trade-offs
