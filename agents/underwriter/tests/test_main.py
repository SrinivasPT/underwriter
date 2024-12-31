from app.database import process_pending_requests
import pytest


# @pytest.mark.skip(reason="Under development")
def test_process_pending_requests():
    process_pending_requests()
