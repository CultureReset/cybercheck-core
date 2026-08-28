-- Illustrative early-stage PostgreSQL projection.
create materialized view business_public_projection as
select b.business_id, b.public_slug, b.display_name
from businesses b
where b.status = 'active';
-- Expand with locations, hours, services, media, events and public availability.
-- Later, stream definitions can move projection evaluation into a dedicated service.
