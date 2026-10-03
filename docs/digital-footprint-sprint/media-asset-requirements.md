# Media Asset Requirements

Date checked: 2026-07-06

Purpose: define the missing media needed to make the website, LinkedIn, YouTube,
Instagram, Facebook, X, TikTok, and Bluesky profiles visually consistent.

## Current State

The local sprint folders for selected source media are intentionally empty:

| Folder | Needed input |
|---|---|
| `selected_source_photos/` | 10 to 20 owned photo candidates |
| `selected_source_video/` | 3 to 5 speaking, teaching, or audit video candidates |
| `selected_source_audio/` | 1 to 2 clean Michael voice/audio candidates |

The workbook contains 55 asset placeholder rows covering exact destination,
dimensions, video lengths, source candidates, missing inputs, and public-use
gates.

## Placeholder Tokens

| Token | Required asset | Destination |
|---|---|---|
| `[[ASSET:GLOBAL_HEADSHOT_2048_SQ]]` | 2048x2048 master Michael headshot | All profile-photo crops |
| `[[ASSET:GLOBAL_WORKSHOP_LANDSCAPE_2400x1350]]` | 2400x1350 workshop/AI systems landscape | Website hero, social banners, YouTube banner source |
| `[[ASSET:GLOBAL_VERTICAL_REEL_1080x1920]]` | 1080x1920 vertical video template | Instagram Reels, TikTok, YouTube Shorts, Facebook Reels |
| `[[ASSET:GLOBAL_SQUARE_PROOF_CARD_1080]]` | 1080x1080 proof-card template | Instagram grid, LinkedIn carousel, Facebook posts, website cards |
| `[[VIDEO:SPEAKER_REEL_60_90]]` | 60-90 second speaker reel | Website, LinkedIn Featured, YouTube channel trailer source |
| `[[VIDEO:TESTIMONIAL_CHRIS_MOONRAKER_15_30]]` | 15-30 second testimonial clip | Website, speaker reel, Reels/Shorts |
| `[[VIDEO:TESTIMONIAL_CARL_LCR_15_30]]` | 15-30 second testimonial clip | Website, speaker reel, Reels/Shorts |

## Missing Source Media

| Need | Exact requirement | First destination |
|---|---|---|
| Headshot source | 10-20 owned photos or one approved current headshot; face centered, clean lighting | LinkedIn personal, YouTube, Instagram, Facebook, X, TikTok, Bluesky |
| Workshop/teaching landscape | 1-3 owned or public-approved event photos; landscape preferred | Website hero, LinkedIn banner, YouTube banner, Facebook covers |
| Workshop/speaking video | 3-5 clips, with at least one clean speaking segment and one room/prototype segment | Speaker reel and vertical reels |
| Testimonial source clips | Original Chris and Carl video/audio if available | Website testimonials and speaker reel |
| Clean voice/audio | 1-2 clean Michael audio references, 30-120 seconds each | Captions, narration drafts, internal voice tests |

## Generation Path

Free-first:

- use owned photos as the base for profile images and banners;
- use local or open-source image tools for background cleanup and crops;
- use local video tooling for clipping, captions, resizing, and silence removal;
- use transcription first, then use AI writing tools to create captions, hooks, and summaries.

Paid or freemium only when it saves time:

- Canva for rapid resizing and layout;
- OpenAI image tools for final controlled banners if credits/API access are available;
- CapCut or equivalent editor for short proof clips;
- avatar/video tools only after image, voice, face, and public-use permission is clean.

## Public-Use Gate

Do not publish or upload generated media if the source includes:

- attendee faces without permission;
- private client material;
- third-party logos without approval;
- screens with account data;
- private dashboards;
- personal voice samples without explicit intended-use approval.
