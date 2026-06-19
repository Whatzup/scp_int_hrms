from django import forms
from django.forms import inlineformset_factory

from .models import Client, Employee, EmployeeSkill, Project, Site, Task


class EmployeeForm(forms.ModelForm):
    employee_code_preview = forms.CharField(
        disabled=True,
        label='Employee code',
        required=False,
        help_text='Auto-generated when the employee is saved.',
    )

    class Meta:
        model = Employee
        fields = [
            'aadhar_number',
            'first_name',
            'last_name',
            'date_of_birth',
            'gender',
            'email',
            'phone',
            'address',
            'city',
            'state',
            'postal_code',
            'hire_date',
            'employment_status',
            'department_name',
            'manager',
            'job_title',
            'daily_wage',
            'daily_incentive_earned',
            'profile_photo',
            'service_area',
            'plate_number',
            'make',
            'model',
            'year',
            'availability',
            'status',
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'hire_date': forms.DateInput(attrs={'type': 'date'}),
            'issue_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'aadhar_number': 'Aadhaar number',
            'first_name': 'First name',
            'last_name': 'Last name',
            'date_of_birth': 'Date of birth',
            'gender': 'Gender',
            'email': 'Email',
            'phone': 'Phone number',
            'address': 'Address',
            'city': 'City',
            'state': 'State',
            'postal_code': 'Postal code',
            'hire_date': 'Hire date',
            'employment_status': 'Employment status',
            'department_name': 'Department name',
            'manager': 'Reporting to',
            'job_title': 'Job title',
            'daily_wage': 'Daily wage',
            'daily_incentive_earned': 'Incentive earned for day',
            'profile_photo': 'Profile photo',
            'service_area': 'Service area',
            'plate_number': 'Plate number',
            'make': 'Vehicle make',
            'model': 'Vehicle model',
            'year': 'Vehicle year',
            'availability': 'Availability',
            'status': 'Work status',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['employee_code_preview'].initial = (
            self.instance.employee_code if self.instance and self.instance.pk else Employee.next_employee_code()
        )

    def save(self, commit=True):
        employee = super().save(commit=False)
        employee.name = f'{employee.first_name} {employee.last_name}'.strip() or employee.email
        employee.title = employee.get_job_title_display() if employee.job_title else 'HVAC Employee'
        employee.department = employee.department_name.name if employee.department_name else 'HVAC'
        employee.department_id = employee.department_name.name if employee.department_name else ''

        if commit:
            employee.save()
            self.save_m2m()

        return employee


class EmployeeSkillForm(forms.ModelForm):
    class Meta:
        model = EmployeeSkill
        fields = ['skill_name', 'skill_level', 'certificate_number', 'issuing_authority', 'issue_date']
        widgets = {
            'issue_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'skill_name': 'Skill name',
            'skill_level': 'Skill level',
            'certificate_number': 'Certificate number',
            'issuing_authority': 'Issuing authority',
            'issue_date': 'Issue date',
        }


EmployeeSkillFormSet = inlineformset_factory(
    Employee,
    EmployeeSkill,
    form=EmployeeSkillForm,
    extra=1,
    can_delete=True,
)


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'name',
            'customer_name',
            'service_address',
            'equipment_type',
            'job_type',
            'description',
            'owner',
            'start_date',
            'end_date',
            'status',
        ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


class SiteForm(forms.ModelForm):
    site_code_preview = forms.CharField(
        disabled=True,
        label='Site ID',
        required=False,
        help_text='Auto-generated when the site is saved.',
    )

    class Meta:
        model = Site
        fields = [
            'client',
            'site_name',
            'customer_name',
            'contact_person',
            'contact_phone',
            'contact_email',
            'address',
            'city',
            'state',
            'postal_code',
            'site_type',
            'property_type',
            'service_zone',
            'landmark',
            'access_instructions',
            'preferred_visit_time',
            'equipment_summary',
            'assigned_manager',
            'status',
        ]
        labels = {
            'client': 'Client',
            'site_name': 'Site name',
            'customer_name': 'Customer name',
            'contact_person': 'Contact person',
            'contact_phone': 'Contact phone',
            'contact_email': 'Contact email',
            'address': 'Address',
            'city': 'City',
            'state': 'State',
            'postal_code': 'Postal code',
            'site_type': 'Site type',
            'property_type': 'Property type',
            'service_zone': 'Service zone',
            'landmark': 'Landmark',
            'access_instructions': 'Access instructions',
            'preferred_visit_time': 'Preferred visit time',
            'equipment_summary': 'Equipment summary',
            'assigned_manager': 'Assigned manager',
            'status': 'Status',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['site_code_preview'].initial = (
            self.instance.site_code if self.instance and self.instance.pk else Site.next_site_code()
        )


class ClientForm(forms.ModelForm):
    client_code_preview = forms.CharField(
        disabled=True,
        label='Client ID',
        required=False,
        help_text='Auto-generated when the client is saved.',
    )

    class Meta:
        model = Client
        fields = [
            'client_name',
            'company_name',
            'mobile',
            'email',
            'address',
            'project_name',
            'location',
            'building_type',
            'approx_area',
            'requirement',
            'preferred_hvac_system',
            'current_challenges',
            'budget_range',
            'expected_completion_date',
        ]
        widgets = {
            'expected_completion_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'client_name': 'Client name',
            'company_name': 'Company name',
            'mobile': 'Mobile',
            'email': 'Email',
            'address': 'Address',
            'project_name': 'Project name',
            'location': 'Location',
            'building_type': 'Building type',
            'approx_area': 'Approx area',
            'requirement': 'Requirement',
            'preferred_hvac_system': 'Preferred HVAC system',
            'current_challenges': 'Current challenges',
            'budget_range': 'Budget range',
            'expected_completion_date': 'Expected completion date',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['client_code_preview'].initial = (
            self.instance.client_code if self.instance and self.instance.pk else Client.next_client_code()
        )


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'project', 'assignee', 'due_date', 'priority', 'status']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }
