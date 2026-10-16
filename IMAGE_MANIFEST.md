# IMAGE_MANIFEST.md

바이브 코딩 실전 — 이미지 목록과 검수 기록 (기준일 2026-10-14, 제작일 2026-10-16)

생성 방식: tools/make_images.py (PIL 기반), Noto CJK 폰트
(/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc, NotoSansCJK-Regular.ttc)

## 이미지 목록

| 파일 | 크기 | 용도 | 본문 참조 위치 |
|---|---|---|---|
| assets/cover.png | 1000x1300 | 표지 (제목·부제·저자·기준일) | pages/00-first-page.md |
| assets/fig-vs-dev.png | 1500x760 | 바이브 코딩 vs 기존 개발 흐름 비교 | pages/11-vibe-vs-traditional.md |
| assets/fig-failure-1.png | 1400x700 | 실패 패턴 1: 환각 코드 | pages/12-failure-patterns.md |
| assets/fig-failure-2.png | 1400x700 | 실패 패턴 2: 보안 구멍 | pages/12-failure-patterns.md |
| assets/fig-failure-3.png | 1400x700 | 실패 패턴 3: 유지보수 부채 | pages/12-failure-patterns.md |
| assets/fig-spec-template.png | 1500x760 | AI가 이해하는 명세서 5요소 구조도 | pages/21-spec-templates.md |
| assets/fig-small-tasks.png | 1500x700 | 큰 요청 vs 작은 요청 나누기 예시 | pages/30-small-tasks.md |
| assets/fig-debug-flow.png | 1500x720 | 디버깅 대화 흐름 | pages/31-debugging-conversation.md |
| assets/fig-deploy-flow.png | 1500x700 | GitHub→무료 호스팅 배포 흐름 | pages/40-project-portfolio.md |
| assets/fig-maintenance.png | 1500x700 | 월 30분 최소 관리 루틴 | pages/50-maintenance-cost.md |

## 검수 기록 (2026-10-16)

- 표지 1000x1300 확인: PIL로 실제 크기 검증 완료 (1000, 1300)
- 본문 도식 9종: 전부 1200x800 내외, PNG 형식, 한글 텍스트 정상 렌더링
- 본문 참조 무결성: pages 내 `../assets/*.png` 참조 10건 전부에 대응하는 파일이 assets/에 존재함을 스크립트로 확인
- 미참조 이미지: 없음 (cover.png 제외 모든 도식이 본문에서 참조됨)
- 미존재 참조: 없음
- 이미지 파일명에 한글·특수문자: 없음
- 검수자 메모: 12장의 실패 패턴 3종 도식은 각각 원인→증상→예방 구조로 통일. 21장 명세서 구조도는 20·21장 본문의 5요소와 일치. 추가 이미지 필요 시 tools/make_images.py에 함수를 추가하고 이 표를 갱신한다.
