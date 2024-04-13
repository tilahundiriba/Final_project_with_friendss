from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from admin_app.models import UserProfileInfo2,Notification
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
@login_required
def tech_profile(request):
    user = request.user
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
    return render(request, 'laboratory_dash/profile.html', {'user': user,'notifications':notifications,
                                                'unseen_count':unseen_count})

@login_required
def tech_profile_update(request, user_id):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
    user = get_object_or_404(User, pk=user_id)
    if request.user != user:  # Ensure user can only update their own profile
        return redirect('show_tech_profile')
    
    user_profile, created = UserProfileInfo2.objects.get_or_create(user=user)
    
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        user_profile.profile_pic = profile_pic
        user_profile.save()
        return redirect('show_tech_profile')
    
    return render(request, 'laboratory_dash/update_profile.html', {'user_id': user_id, 
                                                                   'user_profile': user_profile,'notifications':notifications,
                                                'unseen_count':unseen_count})

def dis_lab_dash(request):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
    return render(request, 'laboratory_dash/lab_dashboard.html',{'notifications':notifications,
                                                'unseen_count':unseen_count})
def dis_lab_dash_content(request):
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
    return render(request, 'laboratory_dash/lab_dash_content.html',{'notifications':notifications,
                                                'unseen_count':unseen_count})