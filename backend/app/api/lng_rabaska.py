"""
API endpoints for LNG Quebec Rabaska parameters.
Provides REST API access to favorable parameters for the LNG project.
"""

from fastapi import APIRouter, Query, HTTPException
from typing import Optional
from app.core.lng_rabaska import (
    get_favorable_parameters,
    get_parameter_category,
    get_summary,
    get_compliance_checklist
)

router = APIRouter(
    prefix="/lng-rabaska",
    tags=["lng-rabaska"]
)


@router.get("/parameters")
def get_parameters():
    """
    Retrieve all favorable parameters for LNG Quebec Rabaska project.
    
    Returns comprehensive parameters covering environmental, economic,
    regulatory, technical, and social aspects.
    """
    return get_favorable_parameters()


@router.get("/parameters/{category}")
def get_category_parameters(category: str):
    """
    Retrieve parameters for a specific category.
    
    Args:
        category: Category name (environmental, economic, regulatory, technical, social)
    
    Returns:
        Parameters for the specified category.
    
    Raises:
        HTTPException: If category not found.
    """
    result = get_parameter_category(category)
    if result is None:
        raise HTTPException(
            status_code=404,
            detail=f"Category '{category}' not found. Valid categories: environmental, economic, regulatory, technical, social"
        )
    return result


@router.get("/summary")
def get_project_summary():
    """
    Retrieve a summary of favorable parameters.
    
    Returns:
        High-level summary with key highlights from each category.
    """
    return get_summary()


@router.get("/compliance")
def get_compliance():
    """
    Retrieve compliance checklist for the project.
    
    Returns:
        List of compliance items with their status and priority.
    """
    return {
        "project": "LNG Québec Rabaska",
        "checklist": get_compliance_checklist()
    }


@router.get("/health")
def health_check():
    """
    Health check endpoint for LNG Rabaska module.
    
    Returns:
        Status information.
    """
    return {
        "module": "lng-rabaska",
        "status": "operational",
        "endpoints": [
            "/lng-rabaska/parameters",
            "/lng-rabaska/parameters/{category}",
            "/lng-rabaska/summary",
            "/lng-rabaska/compliance",
            "/lng-rabaska/health"
        ]
    }
