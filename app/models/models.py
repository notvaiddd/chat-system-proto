

from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from ..database import Base
import datetime
import uuid

class User(Base):
    """SQLAlchemy model for the 'users' table."""
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), default=datetime.datetime.utcnow)

    sessions = relationship("Session", back_populates="user")

class Session(Base):
    """SQLAlchemy model for the 'sessions' table."""
    __tablename__ = "sessions"

    session_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    start_time = Column(TIMESTAMP(timezone=True), default=datetime.datetime.utcnow)
    end_time = Column(TIMESTAMP(timezone=True))
    overall_score = Column(Integer)

    user = relationship("User", back_populates="sessions")
    assessments = relationship("Assessment", back_populates="session")

class Pose(Base):
    """SQLAlchemy model for the 'poses' table."""
    __tablename__ = "poses"

    pose_id = Column(Integer, primary_key=True, index=True)
    pose_name = Column(String, unique=True, nullable=False)
    reference_image = Column(String)

class Assessment(Base):
    """SQLAlchemy model for the 'assessments' table."""
    __tablename__ = "assessments"

    assessment_id = Column(Integer, primary_key=True, index=True)
    session_id = Column(UUID(as_uuid=True), ForeignKey("sessions.session_id"), nullable=False)
    pose_id = Column(Integer, ForeignKey("poses.pose_id"), nullable=False)
    score = Column(Integer)
    feedback = Column(Text)

    session = relationship("Session", back_populates="assessments")
