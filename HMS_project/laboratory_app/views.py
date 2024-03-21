from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from admin_app.models import UserProfileInfo2
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
@login_required
def profile(request):
    user = request.user
    return render(request, 'laboratory_dash/profile.html', {'user': user})

@login_required
def profile_update(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.user != user:  # Ensure user can only update their own profile
        return redirect('show_tech_profile')
    
    user_profile, created = UserProfileInfo2.objects.get_or_create(user=user)
    
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        user_profile.profile_pic = profile_pic
        user_profile.save()
        return redirect('show_tech_profile')
    
    return render(request, 'laboratory_dash/update_profile.html', {'user_id': user_id, 'user_profile': user_profile})

def dis_lab_dash(request):
    return render(request, 'laboratory_dash/lab_dashboard.html')
def dis_lab_dash_content(request):
    return render(request, 'laboratory_dash/lab_dash_content.html')