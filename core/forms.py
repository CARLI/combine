from django.forms import ModelForm

# import models from core for forms
from core.models import Organization, RecordGroup, RecordIdentifierTransformation,\
    Transformation, ValidationScenario, OAIEndpoint, FieldMapper


class OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        fields = ['name', 'description']


class RecordGroupForm(ModelForm):
    class Meta:
        model = RecordGroup
        fields = ['organization', 'name', 'description']


class ValidationScenarioForm(ModelForm):

    class Meta:
        model = ValidationScenario
        fields = ['name', 'payload', 'validation_type', 'default_run']
        labels = {
            'payload': 'Validation Code'
        }


class TransformationForm(ModelForm):

    class Meta:
        model = Transformation
        fields = ['name', 'payload', 'transformation_type', 'use_as_include']
        labels = {
            'payload': 'Transformation Code'
        }


class RITSForm(ModelForm):

    class Meta:
        model = RecordIdentifierTransformation
        fields = ['name', 'transformation_type', 'transformation_target', 'regex_match_payload',
                  'regex_replace_payload', 'python_payload', 'xpath_payload']
        labels = {
            'regex_match_payload': 'Regex to Match',
            'regex_replace_payload': 'Regex Replacement',
            'python_payload': 'Python Code',
            'xpath_payload': 'XPath Query'
        }


class OAIEndpointForm(ModelForm):

    class Meta:
        model = OAIEndpoint
        fields = ['name', 'endpoint', 'metadataPrefix', 'scope_type', 'scope_value']


class FieldMapperForm(ModelForm):

    class Meta:
        model = FieldMapper
        fields = ['name', 'payload', 'config_json', 'field_mapper_type']
        labels = {
            'payload': 'Field Mapping Code'
        }
