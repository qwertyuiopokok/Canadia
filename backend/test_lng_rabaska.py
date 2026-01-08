#!/usr/bin/env python3
"""
Simple test script for LNG Rabaska parameters module.
This script can be run without FastAPI to verify the core functionality.
"""

import sys
import os
import json

# Add backend to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from app.core.lng_rabaska import (
    get_favorable_parameters,
    get_parameter_category,
    get_summary,
    get_compliance_checklist
)


def test_get_favorable_parameters():
    """Test getting all favorable parameters."""
    print("=" * 80)
    print("TEST: get_favorable_parameters()")
    print("=" * 80)
    params = get_favorable_parameters()
    
    # Verify structure
    assert "project_name" in params
    assert params["project_name"] == "LNG Québec Rabaska"
    assert "location" in params
    assert "environmental_parameters" in params
    assert "economic_parameters" in params
    assert "regulatory_parameters" in params
    assert "technical_parameters" in params
    assert "social_parameters" in params
    assert params["status"] == "favorable"
    
    print(f"✓ Project: {params['project_name']}")
    print(f"✓ Location: {params['location']['municipality']}, {params['location']['province']}")
    print(f"✓ Status: {params['status']}")
    print(f"✓ All parameter categories present")
    print("\nSample - Environmental Parameters:")
    print(json.dumps(params["environmental_parameters"], indent=2, ensure_ascii=False))
    print("\n✓ TEST PASSED\n")
    return True


def test_get_parameter_category():
    """Test getting parameters by category."""
    print("=" * 80)
    print("TEST: get_parameter_category()")
    print("=" * 80)
    
    categories = ["environmental", "economic", "regulatory", "technical", "social"]
    
    for category in categories:
        result = get_parameter_category(category)
        assert result is not None, f"Category {category} should return data"
        assert "category" in result
        assert result["category"] == category
        assert "parameters" in result
        assert "project" in result
        assert "location" in result
        print(f"✓ Category '{category}' works correctly")
    
    # Test invalid category
    invalid = get_parameter_category("invalid_category")
    assert invalid is None, "Invalid category should return None"
    print("✓ Invalid category returns None as expected")
    
    # Show example
    print("\nSample - Economic Parameters:")
    economic = get_parameter_category("economic")
    print(json.dumps(economic, indent=2, ensure_ascii=False))
    
    print("\n✓ TEST PASSED\n")
    return True


def test_get_summary():
    """Test getting project summary."""
    print("=" * 80)
    print("TEST: get_summary()")
    print("=" * 80)
    
    summary = get_summary()
    
    assert "project" in summary
    assert "location" in summary
    assert "status" in summary
    assert "highlights" in summary
    assert summary["status"] == "favorable"
    
    highlights = summary["highlights"]
    assert "environmental" in highlights
    assert "economic" in highlights
    assert "regulatory" in highlights
    assert "technical" in highlights
    assert "social" in highlights
    
    print("Summary:")
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    
    print("\n✓ TEST PASSED\n")
    return True


def test_get_compliance_checklist():
    """Test getting compliance checklist."""
    print("=" * 80)
    print("TEST: get_compliance_checklist()")
    print("=" * 80)
    
    checklist = get_compliance_checklist()
    
    assert isinstance(checklist, list), "Checklist should be a list"
    assert len(checklist) > 0, "Checklist should not be empty"
    
    # Verify structure of each item
    for item in checklist:
        assert "item" in item
        assert "status" in item
        assert "level" in item
        assert "priority" in item
        print(f"✓ {item['item']}: {item['status']} ({item['priority']} priority)")
    
    # Check for critical items
    critical_items = [i for i in checklist if i["priority"] == "critical"]
    assert len(critical_items) > 0, "Should have at least one critical item"
    print(f"\n✓ Found {len(critical_items)} critical compliance items")
    
    print("\n✓ TEST PASSED\n")
    return True


def run_all_tests():
    """Run all tests."""
    print("\n" + "=" * 80)
    print("RUNNING ALL TESTS FOR LNG RABASKA MODULE")
    print("=" * 80 + "\n")
    
    tests = [
        test_get_favorable_parameters,
        test_get_parameter_category,
        test_get_summary,
        test_get_compliance_checklist
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
        except AssertionError as e:
            print(f"✗ TEST FAILED: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ TEST ERROR: {e}")
            failed += 1
    
    print("\n" + "=" * 80)
    print(f"RESULTS: {passed} passed, {failed} failed")
    print("=" * 80 + "\n")
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
