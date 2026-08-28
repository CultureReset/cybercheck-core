# Design System and Surface Registry

The UI should feel like one operating system even though independent apps can contribute their own routes and controls.

## Source-grounded rules
- Dashboard navigation should be registry-driven so installed applications can contribute dashboard/settings/onboarding surfaces.
- Data and presentation are separate: the same structured data can render through multiple profile templates.
- Apps should register surfaces rather than requiring hardcoded dashboard code.

## This subsystem owns
- global navigation shell
- shared component vocabulary
- surface registration contract
- accessibility behavior
- mobile interaction patterns

## Core objects / data
- `Surface`
- `SurfaceRegistration`
- `NavigationItem`
- `PermissionGate`
- `DataBinding`
- `ActionBinding`

## Main flow

```text
Installed app manifest
      ↓
surface registration
      ↓
dashboard shell resolves route/navigation
      ↓
permission gate
      ↓
app UI reads projection / invokes capability
```

## UI / UX surfaces
- CyberButton
- CyberCard
- CyberDataField
- CyberSourceBadge
- CyberConfidenceBadge
- CyberPermissionGate
- CyberCapabilityButton
- CyberReceipt
- CyberTimeline
- CyberSearchResult
- CyberMediaCard
- CyberCalendar
- CyberMapCard
- CyberEmptyState
- CyberErrorState
- CyberLoadingState

## Required states and failures
- No permission
- App disabled
- App updating
- Route removed after uninstall
- Slow projection
- Offline device
- Empty dataset
- Partial data
- Mobile narrow screen

## Definition of done
- [ ] All core surfaces share tokens and interaction patterns
- [ ] Apps can register navigation without modifying the dashboard shell
- [ ] Every action control can show policy/approval state
- [ ] Every data field can expose source/provenance when relevant
- [ ] Every primary screen has loading/empty/error/offline states

## Source basis
- text 9.txt — registry-driven dashboard modules and installed surfaces
- text 4(2).txt — data/design separation and templates
- text 6(3).txt — shared frontend component architecture
