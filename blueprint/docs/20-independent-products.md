# Independent Product Layer

Booking, menus, reviews, communications, QR, maps, loyalty and other products bind to platform data and capabilities but are not required for CyberCheck to exist.

## Source-grounded rules
- Universal booking engine is a product using canonical structured tables, not Core.
- Google Business/Meta connectors should be separate products/adapters.
- Industry differences should be contracts/data packages rather than giant switch statements.

## This subsystem owns
- product-specific workflows
- product datasets where operationally appropriate
- product surfaces
- product capabilities
- product events

## Core objects / data
- `booking`
- `availability`
- `menus`
- `reviews`
- `communications`
- `events`
- `qr`
- `loyalty`
- `recommendations`
- `publisher_connectors`

## Main flow

```text
install product → bind required datasets → register surfaces/capabilities → product operates → emits events / reads canonical data
uninstall → disable product → canonical shared data remains
```

## UI / UX surfaces
- Booking/calendar
- Availability
- Menu manager
- Review center
- Communications
- QR/widget
- Map/discovery
- Loyalty/recommendations

## Required states and failures
- Product-specific provider outage
- Product uninstalled
- Dataset permission revoked
- Version incompatibility

## Definition of done
- [ ] Each product can be disabled independently
- [ ] Product code does not modify Core schema ownership rules
- [ ] Product surfaces come from registrations
- [ ] Shared canonical data survives uninstall

## Source basis
- text 9.txt — independent products and extraction of booking/Google/SMS/email parsers
