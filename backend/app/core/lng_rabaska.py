"""
Core logic for LNG Quebec Rabaska parameters.
This module provides favorable parameters and information for the LNG Quebec Rabaska project.
"""

from typing import Dict, List, Any, Optional
from datetime import datetime


def get_favorable_parameters() -> Dict[str, Any]:
    """
    Returns favorable parameters for the LNG Quebec Rabaska project.
    
    Returns:
        Dictionary containing favorable parameters including environmental,
        economic, regulatory, and technical aspects.
    """
    return {
        "project_name": "LNG Québec Rabaska",
        "location": {
            "province": "QC",
            "region": "Lévis",
            "municipality": "Ville de Lévis"
        },
        "environmental_parameters": {
            "emission_reduction_target": {
                "co2_reduction_percentage": 30,
                "description": "Réduction de 30% des émissions de CO2 par rapport aux normes de base"
            },
            "water_treatment": {
                "level": "advanced",
                "recycling_rate": 85,
                "description": "Traitement avancé avec taux de recyclage de 85%"
            },
            "noise_control": {
                "max_decibels": 55,
                "monitoring": "continuous",
                "description": "Contrôle du bruit avec surveillance continue, max 55 dB"
            },
            "air_quality": {
                "monitoring_stations": 5,
                "standards": "exceeds_provincial",
                "description": "5 stations de surveillance, dépassant les normes provinciales"
            }
        },
        "economic_parameters": {
            "job_creation": {
                "construction_phase": 2500,
                "operational_phase": 250,
                "description": "2500 emplois en construction, 250 emplois permanents"
            },
            "local_investment": {
                "percentage": 60,
                "amount_millions": 500,
                "description": "60% d'investissement local, 500M$ dans l'économie régionale"
            },
            "tax_revenue": {
                "annual_millions": 75,
                "description": "75M$ de revenus fiscaux annuels pour la province"
            }
        },
        "regulatory_parameters": {
            "compliance": {
                "federal": "BAPE approved",
                "provincial": "MELCC certified",
                "municipal": "city council approved",
                "description": "Conformité complète avec tous les niveaux gouvernementaux"
            },
            "safety_standards": {
                "certifications": ["ISO 14001", "ISO 45001", "API 620"],
                "inspection_frequency": "quarterly",
                "description": "Certifications internationales avec inspections trimestrielles"
            },
            "community_consultation": {
                "sessions_completed": 25,
                "stakeholder_groups": 15,
                "approval_rate": 72,
                "description": "25 séances de consultation, taux d'approbation de 72%"
            }
        },
        "technical_parameters": {
            "capacity": {
                "annual_tonnes": 14_400_000,
                "storage_capacity_m3": 300000,
                "description": "Capacité annuelle de 14,4 millions de tonnes"
            },
            "infrastructure": {
                "terminals": 2,
                "loading_berths": 3,
                "pipeline_km": 40,
                "description": "2 terminaux, 3 quais de chargement, 40km de pipeline"
            },
            "technology": {
                "liquefaction_process": "advanced_cascaded",
                "energy_efficiency": 92,
                "description": "Processus de liquéfaction en cascade avec efficacité de 92%"
            }
        },
        "social_parameters": {
            "community_benefits": {
                "annual_fund_millions": 5,
                "education_programs": 10,
                "infrastructure_improvements": 15,
                "description": "Fonds communautaire de 5M$/an, 10 programmes éducatifs"
            },
            "indigenous_partnership": {
                "agreements_signed": 3,
                "employment_target_percentage": 15,
                "description": "3 ententes avec communautés autochtones, objectif 15% emploi"
            }
        },
        "timestamp": datetime.now().isoformat(),
        "status": "favorable",
        "version": "1.0"
    }


def get_parameter_category(category: str) -> Optional[Dict[str, Any]]:
    """
    Returns parameters for a specific category.
    
    Args:
        category: The category of parameters to retrieve
                 (environmental, economic, regulatory, technical, social)
    
    Returns:
        Dictionary containing parameters for the specified category,
        or None if category not found.
    """
    all_params = get_favorable_parameters()
    category_key = f"{category}_parameters"
    
    if category_key in all_params:
        return {
            "category": category,
            "parameters": all_params[category_key],
            "project": all_params["project_name"],
            "location": all_params["location"]
        }
    
    return None


def get_summary() -> Dict[str, Any]:
    """
    Returns a summary of favorable parameters for LNG Quebec Rabaska.
    
    Returns:
        Dictionary containing summary information.
    """
    params = get_favorable_parameters()
    
    return {
        "project": params["project_name"],
        "location": f"{params['location']['municipality']}, {params['location']['province']}",
        "status": params["status"],
        "highlights": {
            "environmental": f"Réduction CO2 de {params['environmental_parameters']['emission_reduction_target']['co2_reduction_percentage']}%",
            "economic": f"{params['economic_parameters']['job_creation']['operational_phase']} emplois permanents",
            "regulatory": f"Taux d'approbation communautaire de {params['regulatory_parameters']['community_consultation']['approval_rate']}%",
            "technical": f"Capacité annuelle de {params['technical_parameters']['capacity']['annual_tonnes']:,} tonnes",
            "social": f"Fonds communautaire de {params['social_parameters']['community_benefits']['annual_fund_millions']}M$/an"
        },
        "timestamp": params["timestamp"],
        "version": params["version"]
    }


def get_compliance_checklist() -> List[Dict[str, Any]]:
    """
    Returns a compliance checklist for the project.
    
    Returns:
        List of compliance items with their status.
    """
    return [
        {
            "item": "Évaluation environnementale BAPE",
            "status": "completed",
            "level": "federal",
            "priority": "critical"
        },
        {
            "item": "Certification MELCC",
            "status": "completed",
            "level": "provincial",
            "priority": "critical"
        },
        {
            "item": "Approbation conseil municipal",
            "status": "completed",
            "level": "municipal",
            "priority": "high"
        },
        {
            "item": "Certification ISO 14001",
            "status": "completed",
            "level": "international",
            "priority": "high"
        },
        {
            "item": "Certification ISO 45001",
            "status": "completed",
            "level": "international",
            "priority": "high"
        },
        {
            "item": "Consultation communautaire",
            "status": "completed",
            "level": "community",
            "priority": "critical"
        },
        {
            "item": "Ententes autochtones",
            "status": "completed",
            "level": "community",
            "priority": "critical"
        },
        {
            "item": "Plan de surveillance environnementale",
            "status": "active",
            "level": "operational",
            "priority": "high"
        }
    ]
