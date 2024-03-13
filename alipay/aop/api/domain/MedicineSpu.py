#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MedicineAccessQualification import MedicineAccessQualification
from alipay.aop.api.domain.MedicineAccessQualification import MedicineAccessQualification


class MedicineSpu(object):

    def __init__(self):
        self._administration_method = None
        self._adverse_reactions = None
        self._applicable_age = None
        self._application_scope = None
        self._approval_number = None
        self._brand_name = None
        self._classification = None
        self._common_name = None
        self._contraindications = None
        self._device_common_name = None
        self._device_spec = None
        self._dosage_from = None
        self._efficacies = None
        self._mah = None
        self._main_access_qualification = None
        self._main_category = None
        self._main_image = None
        self._main_ingredients = None
        self._management_category = None
        self._manufacturer_name = None
        self._measurement_unit = None
        self._origin_label = None
        self._origin_place = None
        self._other_access_qualifications = None
        self._other_images = None
        self._physical_properties = None
        self._precautions = None
        self._product_category = None
        self._product_code = None
        self._production_license_number = None
        self._regulatory_classification = None
        self._shelf_life = None
        self._specification = None
        self._storage_conditions = None
        self._structure_composition = None
        self._sub_brand_name = None
        self._suitable_population = None
        self._therapeutic_efficacy = None
        self._trademark_name = None
        self._unsuitable_population = None
        self._upc = None
        self._usage_method_amount = None

    @property
    def administration_method(self):
        return self._administration_method

    @administration_method.setter
    def administration_method(self, value):
        self._administration_method = value
    @property
    def adverse_reactions(self):
        return self._adverse_reactions

    @adverse_reactions.setter
    def adverse_reactions(self, value):
        self._adverse_reactions = value
    @property
    def applicable_age(self):
        return self._applicable_age

    @applicable_age.setter
    def applicable_age(self, value):
        self._applicable_age = value
    @property
    def application_scope(self):
        return self._application_scope

    @application_scope.setter
    def application_scope(self, value):
        self._application_scope = value
    @property
    def approval_number(self):
        return self._approval_number

    @approval_number.setter
    def approval_number(self, value):
        self._approval_number = value
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def classification(self):
        return self._classification

    @classification.setter
    def classification(self, value):
        self._classification = value
    @property
    def common_name(self):
        return self._common_name

    @common_name.setter
    def common_name(self, value):
        self._common_name = value
    @property
    def contraindications(self):
        return self._contraindications

    @contraindications.setter
    def contraindications(self, value):
        self._contraindications = value
    @property
    def device_common_name(self):
        return self._device_common_name

    @device_common_name.setter
    def device_common_name(self, value):
        self._device_common_name = value
    @property
    def device_spec(self):
        return self._device_spec

    @device_spec.setter
    def device_spec(self, value):
        self._device_spec = value
    @property
    def dosage_from(self):
        return self._dosage_from

    @dosage_from.setter
    def dosage_from(self, value):
        self._dosage_from = value
    @property
    def efficacies(self):
        return self._efficacies

    @efficacies.setter
    def efficacies(self, value):
        if isinstance(value, list):
            self._efficacies = list()
            for i in value:
                self._efficacies.append(i)
    @property
    def mah(self):
        return self._mah

    @mah.setter
    def mah(self, value):
        self._mah = value
    @property
    def main_access_qualification(self):
        return self._main_access_qualification

    @main_access_qualification.setter
    def main_access_qualification(self, value):
        if isinstance(value, MedicineAccessQualification):
            self._main_access_qualification = value
        else:
            self._main_access_qualification = MedicineAccessQualification.from_alipay_dict(value)
    @property
    def main_category(self):
        return self._main_category

    @main_category.setter
    def main_category(self, value):
        self._main_category = value
    @property
    def main_image(self):
        return self._main_image

    @main_image.setter
    def main_image(self, value):
        self._main_image = value
    @property
    def main_ingredients(self):
        return self._main_ingredients

    @main_ingredients.setter
    def main_ingredients(self, value):
        self._main_ingredients = value
    @property
    def management_category(self):
        return self._management_category

    @management_category.setter
    def management_category(self, value):
        self._management_category = value
    @property
    def manufacturer_name(self):
        return self._manufacturer_name

    @manufacturer_name.setter
    def manufacturer_name(self, value):
        self._manufacturer_name = value
    @property
    def measurement_unit(self):
        return self._measurement_unit

    @measurement_unit.setter
    def measurement_unit(self, value):
        self._measurement_unit = value
    @property
    def origin_label(self):
        return self._origin_label

    @origin_label.setter
    def origin_label(self, value):
        self._origin_label = value
    @property
    def origin_place(self):
        return self._origin_place

    @origin_place.setter
    def origin_place(self, value):
        self._origin_place = value
    @property
    def other_access_qualifications(self):
        return self._other_access_qualifications

    @other_access_qualifications.setter
    def other_access_qualifications(self, value):
        if isinstance(value, list):
            self._other_access_qualifications = list()
            for i in value:
                if isinstance(i, MedicineAccessQualification):
                    self._other_access_qualifications.append(i)
                else:
                    self._other_access_qualifications.append(MedicineAccessQualification.from_alipay_dict(i))
    @property
    def other_images(self):
        return self._other_images

    @other_images.setter
    def other_images(self, value):
        if isinstance(value, list):
            self._other_images = list()
            for i in value:
                self._other_images.append(i)
    @property
    def physical_properties(self):
        return self._physical_properties

    @physical_properties.setter
    def physical_properties(self, value):
        self._physical_properties = value
    @property
    def precautions(self):
        return self._precautions

    @precautions.setter
    def precautions(self, value):
        self._precautions = value
    @property
    def product_category(self):
        return self._product_category

    @product_category.setter
    def product_category(self, value):
        self._product_category = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def production_license_number(self):
        return self._production_license_number

    @production_license_number.setter
    def production_license_number(self, value):
        self._production_license_number = value
    @property
    def regulatory_classification(self):
        return self._regulatory_classification

    @regulatory_classification.setter
    def regulatory_classification(self, value):
        self._regulatory_classification = value
    @property
    def shelf_life(self):
        return self._shelf_life

    @shelf_life.setter
    def shelf_life(self, value):
        self._shelf_life = value
    @property
    def specification(self):
        return self._specification

    @specification.setter
    def specification(self, value):
        self._specification = value
    @property
    def storage_conditions(self):
        return self._storage_conditions

    @storage_conditions.setter
    def storage_conditions(self, value):
        self._storage_conditions = value
    @property
    def structure_composition(self):
        return self._structure_composition

    @structure_composition.setter
    def structure_composition(self, value):
        self._structure_composition = value
    @property
    def sub_brand_name(self):
        return self._sub_brand_name

    @sub_brand_name.setter
    def sub_brand_name(self, value):
        self._sub_brand_name = value
    @property
    def suitable_population(self):
        return self._suitable_population

    @suitable_population.setter
    def suitable_population(self, value):
        self._suitable_population = value
    @property
    def therapeutic_efficacy(self):
        return self._therapeutic_efficacy

    @therapeutic_efficacy.setter
    def therapeutic_efficacy(self, value):
        self._therapeutic_efficacy = value
    @property
    def trademark_name(self):
        return self._trademark_name

    @trademark_name.setter
    def trademark_name(self, value):
        self._trademark_name = value
    @property
    def unsuitable_population(self):
        return self._unsuitable_population

    @unsuitable_population.setter
    def unsuitable_population(self, value):
        self._unsuitable_population = value
    @property
    def upc(self):
        return self._upc

    @upc.setter
    def upc(self, value):
        self._upc = value
    @property
    def usage_method_amount(self):
        return self._usage_method_amount

    @usage_method_amount.setter
    def usage_method_amount(self, value):
        self._usage_method_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.administration_method:
            if hasattr(self.administration_method, 'to_alipay_dict'):
                params['administration_method'] = self.administration_method.to_alipay_dict()
            else:
                params['administration_method'] = self.administration_method
        if self.adverse_reactions:
            if hasattr(self.adverse_reactions, 'to_alipay_dict'):
                params['adverse_reactions'] = self.adverse_reactions.to_alipay_dict()
            else:
                params['adverse_reactions'] = self.adverse_reactions
        if self.applicable_age:
            if hasattr(self.applicable_age, 'to_alipay_dict'):
                params['applicable_age'] = self.applicable_age.to_alipay_dict()
            else:
                params['applicable_age'] = self.applicable_age
        if self.application_scope:
            if hasattr(self.application_scope, 'to_alipay_dict'):
                params['application_scope'] = self.application_scope.to_alipay_dict()
            else:
                params['application_scope'] = self.application_scope
        if self.approval_number:
            if hasattr(self.approval_number, 'to_alipay_dict'):
                params['approval_number'] = self.approval_number.to_alipay_dict()
            else:
                params['approval_number'] = self.approval_number
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.classification:
            if hasattr(self.classification, 'to_alipay_dict'):
                params['classification'] = self.classification.to_alipay_dict()
            else:
                params['classification'] = self.classification
        if self.common_name:
            if hasattr(self.common_name, 'to_alipay_dict'):
                params['common_name'] = self.common_name.to_alipay_dict()
            else:
                params['common_name'] = self.common_name
        if self.contraindications:
            if hasattr(self.contraindications, 'to_alipay_dict'):
                params['contraindications'] = self.contraindications.to_alipay_dict()
            else:
                params['contraindications'] = self.contraindications
        if self.device_common_name:
            if hasattr(self.device_common_name, 'to_alipay_dict'):
                params['device_common_name'] = self.device_common_name.to_alipay_dict()
            else:
                params['device_common_name'] = self.device_common_name
        if self.device_spec:
            if hasattr(self.device_spec, 'to_alipay_dict'):
                params['device_spec'] = self.device_spec.to_alipay_dict()
            else:
                params['device_spec'] = self.device_spec
        if self.dosage_from:
            if hasattr(self.dosage_from, 'to_alipay_dict'):
                params['dosage_from'] = self.dosage_from.to_alipay_dict()
            else:
                params['dosage_from'] = self.dosage_from
        if self.efficacies:
            if isinstance(self.efficacies, list):
                for i in range(0, len(self.efficacies)):
                    element = self.efficacies[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.efficacies[i] = element.to_alipay_dict()
            if hasattr(self.efficacies, 'to_alipay_dict'):
                params['efficacies'] = self.efficacies.to_alipay_dict()
            else:
                params['efficacies'] = self.efficacies
        if self.mah:
            if hasattr(self.mah, 'to_alipay_dict'):
                params['mah'] = self.mah.to_alipay_dict()
            else:
                params['mah'] = self.mah
        if self.main_access_qualification:
            if hasattr(self.main_access_qualification, 'to_alipay_dict'):
                params['main_access_qualification'] = self.main_access_qualification.to_alipay_dict()
            else:
                params['main_access_qualification'] = self.main_access_qualification
        if self.main_category:
            if hasattr(self.main_category, 'to_alipay_dict'):
                params['main_category'] = self.main_category.to_alipay_dict()
            else:
                params['main_category'] = self.main_category
        if self.main_image:
            if hasattr(self.main_image, 'to_alipay_dict'):
                params['main_image'] = self.main_image.to_alipay_dict()
            else:
                params['main_image'] = self.main_image
        if self.main_ingredients:
            if hasattr(self.main_ingredients, 'to_alipay_dict'):
                params['main_ingredients'] = self.main_ingredients.to_alipay_dict()
            else:
                params['main_ingredients'] = self.main_ingredients
        if self.management_category:
            if hasattr(self.management_category, 'to_alipay_dict'):
                params['management_category'] = self.management_category.to_alipay_dict()
            else:
                params['management_category'] = self.management_category
        if self.manufacturer_name:
            if hasattr(self.manufacturer_name, 'to_alipay_dict'):
                params['manufacturer_name'] = self.manufacturer_name.to_alipay_dict()
            else:
                params['manufacturer_name'] = self.manufacturer_name
        if self.measurement_unit:
            if hasattr(self.measurement_unit, 'to_alipay_dict'):
                params['measurement_unit'] = self.measurement_unit.to_alipay_dict()
            else:
                params['measurement_unit'] = self.measurement_unit
        if self.origin_label:
            if hasattr(self.origin_label, 'to_alipay_dict'):
                params['origin_label'] = self.origin_label.to_alipay_dict()
            else:
                params['origin_label'] = self.origin_label
        if self.origin_place:
            if hasattr(self.origin_place, 'to_alipay_dict'):
                params['origin_place'] = self.origin_place.to_alipay_dict()
            else:
                params['origin_place'] = self.origin_place
        if self.other_access_qualifications:
            if isinstance(self.other_access_qualifications, list):
                for i in range(0, len(self.other_access_qualifications)):
                    element = self.other_access_qualifications[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.other_access_qualifications[i] = element.to_alipay_dict()
            if hasattr(self.other_access_qualifications, 'to_alipay_dict'):
                params['other_access_qualifications'] = self.other_access_qualifications.to_alipay_dict()
            else:
                params['other_access_qualifications'] = self.other_access_qualifications
        if self.other_images:
            if isinstance(self.other_images, list):
                for i in range(0, len(self.other_images)):
                    element = self.other_images[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.other_images[i] = element.to_alipay_dict()
            if hasattr(self.other_images, 'to_alipay_dict'):
                params['other_images'] = self.other_images.to_alipay_dict()
            else:
                params['other_images'] = self.other_images
        if self.physical_properties:
            if hasattr(self.physical_properties, 'to_alipay_dict'):
                params['physical_properties'] = self.physical_properties.to_alipay_dict()
            else:
                params['physical_properties'] = self.physical_properties
        if self.precautions:
            if hasattr(self.precautions, 'to_alipay_dict'):
                params['precautions'] = self.precautions.to_alipay_dict()
            else:
                params['precautions'] = self.precautions
        if self.product_category:
            if hasattr(self.product_category, 'to_alipay_dict'):
                params['product_category'] = self.product_category.to_alipay_dict()
            else:
                params['product_category'] = self.product_category
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.production_license_number:
            if hasattr(self.production_license_number, 'to_alipay_dict'):
                params['production_license_number'] = self.production_license_number.to_alipay_dict()
            else:
                params['production_license_number'] = self.production_license_number
        if self.regulatory_classification:
            if hasattr(self.regulatory_classification, 'to_alipay_dict'):
                params['regulatory_classification'] = self.regulatory_classification.to_alipay_dict()
            else:
                params['regulatory_classification'] = self.regulatory_classification
        if self.shelf_life:
            if hasattr(self.shelf_life, 'to_alipay_dict'):
                params['shelf_life'] = self.shelf_life.to_alipay_dict()
            else:
                params['shelf_life'] = self.shelf_life
        if self.specification:
            if hasattr(self.specification, 'to_alipay_dict'):
                params['specification'] = self.specification.to_alipay_dict()
            else:
                params['specification'] = self.specification
        if self.storage_conditions:
            if hasattr(self.storage_conditions, 'to_alipay_dict'):
                params['storage_conditions'] = self.storage_conditions.to_alipay_dict()
            else:
                params['storage_conditions'] = self.storage_conditions
        if self.structure_composition:
            if hasattr(self.structure_composition, 'to_alipay_dict'):
                params['structure_composition'] = self.structure_composition.to_alipay_dict()
            else:
                params['structure_composition'] = self.structure_composition
        if self.sub_brand_name:
            if hasattr(self.sub_brand_name, 'to_alipay_dict'):
                params['sub_brand_name'] = self.sub_brand_name.to_alipay_dict()
            else:
                params['sub_brand_name'] = self.sub_brand_name
        if self.suitable_population:
            if hasattr(self.suitable_population, 'to_alipay_dict'):
                params['suitable_population'] = self.suitable_population.to_alipay_dict()
            else:
                params['suitable_population'] = self.suitable_population
        if self.therapeutic_efficacy:
            if hasattr(self.therapeutic_efficacy, 'to_alipay_dict'):
                params['therapeutic_efficacy'] = self.therapeutic_efficacy.to_alipay_dict()
            else:
                params['therapeutic_efficacy'] = self.therapeutic_efficacy
        if self.trademark_name:
            if hasattr(self.trademark_name, 'to_alipay_dict'):
                params['trademark_name'] = self.trademark_name.to_alipay_dict()
            else:
                params['trademark_name'] = self.trademark_name
        if self.unsuitable_population:
            if hasattr(self.unsuitable_population, 'to_alipay_dict'):
                params['unsuitable_population'] = self.unsuitable_population.to_alipay_dict()
            else:
                params['unsuitable_population'] = self.unsuitable_population
        if self.upc:
            if hasattr(self.upc, 'to_alipay_dict'):
                params['upc'] = self.upc.to_alipay_dict()
            else:
                params['upc'] = self.upc
        if self.usage_method_amount:
            if hasattr(self.usage_method_amount, 'to_alipay_dict'):
                params['usage_method_amount'] = self.usage_method_amount.to_alipay_dict()
            else:
                params['usage_method_amount'] = self.usage_method_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicineSpu()
        if 'administration_method' in d:
            o.administration_method = d['administration_method']
        if 'adverse_reactions' in d:
            o.adverse_reactions = d['adverse_reactions']
        if 'applicable_age' in d:
            o.applicable_age = d['applicable_age']
        if 'application_scope' in d:
            o.application_scope = d['application_scope']
        if 'approval_number' in d:
            o.approval_number = d['approval_number']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'classification' in d:
            o.classification = d['classification']
        if 'common_name' in d:
            o.common_name = d['common_name']
        if 'contraindications' in d:
            o.contraindications = d['contraindications']
        if 'device_common_name' in d:
            o.device_common_name = d['device_common_name']
        if 'device_spec' in d:
            o.device_spec = d['device_spec']
        if 'dosage_from' in d:
            o.dosage_from = d['dosage_from']
        if 'efficacies' in d:
            o.efficacies = d['efficacies']
        if 'mah' in d:
            o.mah = d['mah']
        if 'main_access_qualification' in d:
            o.main_access_qualification = d['main_access_qualification']
        if 'main_category' in d:
            o.main_category = d['main_category']
        if 'main_image' in d:
            o.main_image = d['main_image']
        if 'main_ingredients' in d:
            o.main_ingredients = d['main_ingredients']
        if 'management_category' in d:
            o.management_category = d['management_category']
        if 'manufacturer_name' in d:
            o.manufacturer_name = d['manufacturer_name']
        if 'measurement_unit' in d:
            o.measurement_unit = d['measurement_unit']
        if 'origin_label' in d:
            o.origin_label = d['origin_label']
        if 'origin_place' in d:
            o.origin_place = d['origin_place']
        if 'other_access_qualifications' in d:
            o.other_access_qualifications = d['other_access_qualifications']
        if 'other_images' in d:
            o.other_images = d['other_images']
        if 'physical_properties' in d:
            o.physical_properties = d['physical_properties']
        if 'precautions' in d:
            o.precautions = d['precautions']
        if 'product_category' in d:
            o.product_category = d['product_category']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'production_license_number' in d:
            o.production_license_number = d['production_license_number']
        if 'regulatory_classification' in d:
            o.regulatory_classification = d['regulatory_classification']
        if 'shelf_life' in d:
            o.shelf_life = d['shelf_life']
        if 'specification' in d:
            o.specification = d['specification']
        if 'storage_conditions' in d:
            o.storage_conditions = d['storage_conditions']
        if 'structure_composition' in d:
            o.structure_composition = d['structure_composition']
        if 'sub_brand_name' in d:
            o.sub_brand_name = d['sub_brand_name']
        if 'suitable_population' in d:
            o.suitable_population = d['suitable_population']
        if 'therapeutic_efficacy' in d:
            o.therapeutic_efficacy = d['therapeutic_efficacy']
        if 'trademark_name' in d:
            o.trademark_name = d['trademark_name']
        if 'unsuitable_population' in d:
            o.unsuitable_population = d['unsuitable_population']
        if 'upc' in d:
            o.upc = d['upc']
        if 'usage_method_amount' in d:
            o.usage_method_amount = d['usage_method_amount']
        return o


