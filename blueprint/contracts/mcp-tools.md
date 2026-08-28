# MCP Surface Draft

## Public MCP
Read-only publishable tools/resources: get_business, search_businesses, get_services, get_availability_public, get_events, get_reviews_public, get_media_public.

## Private MCP
Authenticated tools may include update_hours, update_service, availability_block, booking_read_private, customer_message, facebook_publish, review_reply.

Private MCP is only an interface. Writes still go: MCP → Gateway → Identity/Core → Permission/Capability → Orchestrator → Policy → Approval → Executor → Verification → Receipt.
