# Browser Runtime

The browser runtime is one executor. It should prefer deterministic Playwright-style automation, escalate to semantic/self-healing discovery, and use general agent/vision fallback only when necessary.

## Source-grounded rules
- Browser executor owns interaction mechanics, not business policy.
- Persistent browser profiles can preserve authenticated sessions.
- Successful semantic/general-agent discoveries should be compiled back into deterministic procedures/AppMaps.

## This subsystem owns
- browser workers
- profiles/sessions
- DOM/accessibility interaction
- screenshots/observations
- browser AppMaps
- health checks

## Core objects / data
- `browser_nodes`
- `browser_profiles`
- `browser_sessions`
- `browser_observations`
- `browser_app_maps`

## Main flow

```text
capability request → deterministic DOM/AppMap
      ↓ fail
semantic repair/discovery
      ↓ fail
general computer-use fallback
      ↓
observe + verify → return result
```

## UI / UX surfaces
- Browser profile detail
- Remote view
- Session health
- AppMap targets
- Screenshot evidence
- Repair action

## Required states and failures
- Logged-out session
- 2FA challenge
- DOM redesign
- Popup/modal unexpected
- Network failure
- Bot challenge
- Wrong tenant/account

## Definition of done
- [ ] Browser runtime cannot approve its own action
- [ ] Profile isolation is tenant-safe
- [ ] Runtime returns observations not just click success
- [ ] Unknown screen can stop and request repair/human takeover

## Source basis
- text(20260827-201113).txt — browser levels and persistent computer model
- text 3(3).txt — universal executor hierarchy
