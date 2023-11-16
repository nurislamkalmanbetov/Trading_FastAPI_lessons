from fastapi import APIRouter, BackgroundTasks, Depends

from auth.base_config import current_user

from .tasks import get_email_template_dashboard, send_email_report_dashboard

router = APIRouter(prefix="/report")



@router.get("/dashboard")   ## Celery worker
def get_dashboard_report(user=Depends(current_user)):
    send_email_report_dashboard.delay(user.username)
    return {
        "status": 200,
        "data": "Письмо отправлено",
        "details": None
    }
    
    
# @router.get("/dashboard")    ## without Celery JUST WITH  - BackgroundTasks
# def get_dashboard_report(background_tasks: BackgroundTasks, user=Depends(current_user)):
#     background_tasks.add_task(send_email_report_dashboard,user.username)
#     # send_email_report_dashboard(user.username)
#     return {
#         "status": 200,
#         "data": "Письмо отправлено",
#         "details": None
#     }