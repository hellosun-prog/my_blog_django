# 📝 My Blog Django

> Django 기반의 개인 블로그 웹 애플리케이션

---

## 🔗 Repository

[https://github.com/hellosun-prog/my_blog_django](https://github.com/hellosun-prog/my_blog_django)

---

## 🛠 Tech Stack

| 분류 | 기술 |
|------|------|
| Backend | Python, Django |
| Frontend | Bootstrap 5, HTML/CSS |
| 에디터 | Markdownx (마크다운) |
| 인증 | django-allauth (Google 소셜 로그인) |
| 폼 | django-crispy-forms |
| DB | SQLite (기본) |

---

## ✨ 주요 기능

### 📌 포스트
- 포스트 목록 조회 (페이지네이션, 5개씩)
- 포스트 상세 조회
- 포스트 작성 / 수정 (staff 또는 superuser 권한 필요)
- 마크다운으로 본문 작성
- 헤더 이미지 업로드
- 파일 첨부 기능

### 🏷 카테고리 & 태그
- 카테고리별 포스트 필터링
- 태그별 포스트 필터링
- 미분류(no_category) 포스트 별도 조회

### 🔍 검색
- 제목 또는 태그 이름으로 포스트 검색

### 💬 댓글
- 로그인한 사용자만 댓글 작성 가능
- 본인 댓글 수정 / 삭제

### 🔐 인증
- Google 소셜 로그인 (django-allauth)
- 권한에 따른 접근 제어 (작성은 staff/superuser만)

### 🏠 단일 페이지
- Landing 페이지 (최근 포스트 3개 노출)
- About Me 페이지

---

## 📁 프로젝트 구조

```
my_blog_django/
├── blog/                        # 블로그 앱
│   ├── models.py                # Post, Category, Tag, Comment 모델
│   ├── views.py                 # CBV 기반 뷰 (ListView, DetailView, CreateView 등)
│   ├── urls.py                  # 블로그 URL 라우팅
│   ├── forms.py                 # CommentForm
│   ├── admin.py                 # 관리자 페이지 설정
│   ├── templates/blog/          # HTML 템플릿
│   │   ├── base.html
│   │   ├── post_list.html
│   │   ├── post_detail.html
│   │   ├── post_form.html
│   │   ├── post_update_form.html
│   │   └── comment_form.html
│   └── static/blog/bootstrap/   # Bootstrap CSS
│
├── single_pages/                # 단일 페이지 앱
│   ├── views.py                 # landing, about_me 뷰
│   ├── urls.py
│   └── templates/single_pages/
│       ├── landing.html
│       └── about_me.html
│
├── my_blog_django_proj/         # 프로젝트 설정
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
└── manage.py
```

---

## 🗃 데이터 모델

### Post
| 필드 | 설명 |
|------|------|
| title | 포스트 제목 (최대 30자) |
| hook_text | 짧은 소개 문구 |
| content | 본문 (Markdown) |
| head_image | 헤더 이미지 |
| file_upload | 첨부 파일 |
| author | 작성자 (User FK) |
| category | 카테고리 (FK) |
| tags | 태그 (ManyToMany) |
| created_at / updated_at | 생성/수정 시각 |

### Comment
| 필드 | 설명 |
|------|------|
| post | 연결된 포스트 (FK) |
| author | 작성자 (User FK) |
| content | 댓글 내용 |
| created_at / modified_at | 생성/수정 시각 |

---

## 🚀 실행 방법

```bash
# 1. 의존성 설치
pip install -r requirements.txt

# 2. 마이그레이션
python manage.py migrate

# 3. 슈퍼유저 생성
python manage.py createsuperuser

# 4. 서버 실행
python manage.py runserver
```

> Google 소셜 로그인 사용 시 `settings.py`에 OAuth 클라이언트 ID/Secret 설정 필요

---

## 📌 URL 구조

| URL | 기능 |
|-----|------|
| `/` | 랜딩 페이지 |
| `/about_me/` | About Me |
| `/blog/` | 포스트 목록 |
| `/blog/<pk>/` | 포스트 상세 |
| `/blog/create_post/` | 포스트 작성 |
| `/blog/update_post/<pk>/` | 포스트 수정 |
| `/blog/category/<slug>/` | 카테고리 필터 |
| `/blog/tag/<slug>/` | 태그 필터 |
| `/blog/search/<q>/` | 검색 |
| `/accounts/` | 인증 (allauth) |
| `/admin/` | 관리자 페이지 |
