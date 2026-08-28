# Android and iOS Runtime

Mobile execution follows the same capability contract as browser/API execution while using mobile-specific transports and semantic UI information.

## Source-grounded rules
- Prefer structured accessibility/UI-tree targets over coordinate taps.
- ADB/accessibility is foundational on Android; vision is fallback.
- Shared semantic AppMaps should describe elements by meaning so browser/Android/iOS implementations can differ underneath.

## This subsystem owns
- device transport
- screen/accessibility capture
- input
- mobile AppMaps
- device health
- remote view/human takeover

## Core objects / data
- `mobile_devices`
- `device_apps`
- `mobile_sessions`
- `ui_observations`
- `mobile_app_maps`

## Main flow

```text
capability → device resolver → semantic AppMap target → accessibility/UI tree → ADB/XCUITest action → read back → verify
fallback: screenshot/vision → repair/human takeover
```

## UI / UX surfaces
- Device list
- Device detail
- AppMap screen
- Remote view
- Connection/setup wizard
- Offline/repair state

## Required states and failures
- Device offline
- Accessibility permission removed
- App updated
- UI target missing
- Keyboard/input failure
- Wrong account signed in
- Screen lock

## Definition of done
- [ ] Semantic IDs survive coordinate/layout changes when possible
- [ ] Device actions produce read-back observations
- [ ] Device does not decide permissions
- [ ] Human takeover is available for unknown/blocked state

## Source basis
- text(20260827-201113).txt — Android/iOS executor stack
- text 3(3).txt — browser/Linux/API/MCP/Android/edge abstraction
