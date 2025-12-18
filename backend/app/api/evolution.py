from fastapi import HTTPException

# Approve a source proposal
@router.post("/proposals/{proposal_id}/approve")
def approve_source_proposal(proposal_id: int):
  conn = get_connection()
  cur = conn.cursor()
  cur.execute("""
    UPDATE source_proposals SET status = 'approved' WHERE id = ?
  """, (proposal_id,))
  if cur.rowcount == 0:
    conn.close()
    raise HTTPException(status_code=404, detail="Proposal not found")
  conn.commit()
  conn.close()
  return {"status": "approved", "id": proposal_id}

# Reject a source proposal
@router.post("/proposals/{proposal_id}/reject")
def reject_source_proposal(proposal_id: int):
  conn = get_connection()
  cur = conn.cursor()
  cur.execute("""
    UPDATE source_proposals SET status = 'rejected' WHERE id = ?
  """, (proposal_id,))
  if cur.rowcount == 0:
    conn.close()
    raise HTTPException(status_code=404, detail="Proposal not found")
  conn.commit()
  conn.close()
  return {"status": "rejected", "id": proposal_id}

# List all proposals for a specific gap
@router.get("/gaps/{gap_id}/proposals")
def list_proposals_for_gap(gap_id: int):
  conn = get_connection()
  cur = conn.cursor()
  cur.execute("""
    SELECT id, gap_id, source_name, source_url, method, notes, status, created_at
    FROM source_proposals
    WHERE gap_id = ?
    ORDER BY created_at DESC
  """, (gap_id,))
  rows = cur.fetchall()
  conn.close()
  return [
    {
      "id": r[0],
      "gap_id": r[1],
      "source_name": r[2],
      "source_url": r[3],
      "method": r[4],
      "notes": r[5],
      "status": r[6],
      "created_at": r[7]
    } for r in rows
  ]

# Delete a proposal
@router.delete("/proposals/{proposal_id}")
def delete_source_proposal(proposal_id: int):
  conn = get_connection()
  cur = conn.cursor()
  cur.execute("""
    DELETE FROM source_proposals WHERE id = ?
  """, (proposal_id,))
  if cur.rowcount == 0:
    conn.close()
    raise HTTPException(status_code=404, detail="Proposal not found")
  conn.commit()
  conn.close()
  return {"status": "deleted", "id": proposal_id}
@router.get("/proposals")
def list_source_proposals():
  conn = get_connection()
  cur = conn.cursor()

  cur.execute("""
  SELECT id, gap_id, source_name, source_url, method, notes, status, created_at
  FROM source_proposals
  WHERE status = 'proposed'
  ORDER BY created_at DESC
  """)
  rows = cur.fetchall()
  conn.close()

  return [
    {
      "id": r[0],
      "gap_id": r[1],
      "source_name": r[2],
      "source_url": r[3],
      "method": r[4],
      "notes": r[5],
      "status": r[6],
      "created_at": r[7]
    } for r in rows
  ]
from fastapi import APIRouter
from app.storage.database import get_connection

router = APIRouter(prefix="/admin/evolution", tags=["evolution"])

@router.get("/gaps")
def list_gaps(limit: int = 50):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
      SELECT id, key, theme, province, region, example_question, count, status, priority, updated_at
      FROM gaps
      ORDER BY priority ASC, count DESC
      LIMIT ?
    """, (limit,))
    rows = cur.fetchall()
    conn.close()
    return [
      {
        "id": r[0], "key": r[1], "theme": r[2], "province": r[3], "region": r[4],
        "example_question": r[5], "count": r[6], "status": r[7], "priority": r[8], "updated_at": r[9]
      } for r in rows
    ]
