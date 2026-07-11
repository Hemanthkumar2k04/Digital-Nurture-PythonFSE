from fastapi import FastAPI, Depends, HTTPException, status
from typing import List, Optional
from .schemas import CourseCreate, CourseResponse
from .database import get_db

app = FastAPI(
    title="Course Management API",
    description="High performance async backend utility platform for college records",
    version="1.0"
)

@app.get("/")
async def root():
    return {
        "message": "Course Management API is running"
    }

@app.post("/api/courses/", response_model=CourseResponse, status_code=status.HTTP_201_CREATED)
async def create_course(course: CourseCreate, db: dict = Depends(get_db)):
    new_id = len(db["courses"]) + 1
    course_data = CourseResponse(id=new_id, **course.model_dump())
    db["courses"].append(course_data)
    return course_data

@app.get("/api/courses/", response_model=List[CourseResponse])
async def get_courses(
    skip: int = 0,
    limit: int = 10,
    department_id: Optional[int] = None,
    db: dict = Depends(get_db)
):
    courses = db["courses"]
    if department_id is not None:
        courses = [c for c in courses if c.department_id == department_id]

    return courses[skip: skip + limit]
