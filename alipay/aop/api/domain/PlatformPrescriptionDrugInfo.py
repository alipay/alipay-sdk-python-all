#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PlatformPrescriptionDrugInfo(object):

    def __init__(self):
        self._administration_route = None
        self._comments = None
        self._dosage_form = None
        self._drug_generic_name = None
        self._drug_id = None
        self._drug_name = None
        self._drug_url = None
        self._frequency = None
        self._instructions = None
        self._medicine_quantity = None
        self._single_dose = None
        self._spec = None

    @property
    def administration_route(self):
        return self._administration_route

    @administration_route.setter
    def administration_route(self, value):
        self._administration_route = value
    @property
    def comments(self):
        return self._comments

    @comments.setter
    def comments(self, value):
        self._comments = value
    @property
    def dosage_form(self):
        return self._dosage_form

    @dosage_form.setter
    def dosage_form(self, value):
        self._dosage_form = value
    @property
    def drug_generic_name(self):
        return self._drug_generic_name

    @drug_generic_name.setter
    def drug_generic_name(self, value):
        self._drug_generic_name = value
    @property
    def drug_id(self):
        return self._drug_id

    @drug_id.setter
    def drug_id(self, value):
        self._drug_id = value
    @property
    def drug_name(self):
        return self._drug_name

    @drug_name.setter
    def drug_name(self, value):
        self._drug_name = value
    @property
    def drug_url(self):
        return self._drug_url

    @drug_url.setter
    def drug_url(self, value):
        self._drug_url = value
    @property
    def frequency(self):
        return self._frequency

    @frequency.setter
    def frequency(self, value):
        self._frequency = value
    @property
    def instructions(self):
        return self._instructions

    @instructions.setter
    def instructions(self, value):
        self._instructions = value
    @property
    def medicine_quantity(self):
        return self._medicine_quantity

    @medicine_quantity.setter
    def medicine_quantity(self, value):
        self._medicine_quantity = value
    @property
    def single_dose(self):
        return self._single_dose

    @single_dose.setter
    def single_dose(self, value):
        self._single_dose = value
    @property
    def spec(self):
        return self._spec

    @spec.setter
    def spec(self, value):
        self._spec = value


    def to_alipay_dict(self):
        params = dict()
        if self.administration_route:
            if hasattr(self.administration_route, 'to_alipay_dict'):
                params['administration_route'] = self.administration_route.to_alipay_dict()
            else:
                params['administration_route'] = self.administration_route
        if self.comments:
            if hasattr(self.comments, 'to_alipay_dict'):
                params['comments'] = self.comments.to_alipay_dict()
            else:
                params['comments'] = self.comments
        if self.dosage_form:
            if hasattr(self.dosage_form, 'to_alipay_dict'):
                params['dosage_form'] = self.dosage_form.to_alipay_dict()
            else:
                params['dosage_form'] = self.dosage_form
        if self.drug_generic_name:
            if hasattr(self.drug_generic_name, 'to_alipay_dict'):
                params['drug_generic_name'] = self.drug_generic_name.to_alipay_dict()
            else:
                params['drug_generic_name'] = self.drug_generic_name
        if self.drug_id:
            if hasattr(self.drug_id, 'to_alipay_dict'):
                params['drug_id'] = self.drug_id.to_alipay_dict()
            else:
                params['drug_id'] = self.drug_id
        if self.drug_name:
            if hasattr(self.drug_name, 'to_alipay_dict'):
                params['drug_name'] = self.drug_name.to_alipay_dict()
            else:
                params['drug_name'] = self.drug_name
        if self.drug_url:
            if hasattr(self.drug_url, 'to_alipay_dict'):
                params['drug_url'] = self.drug_url.to_alipay_dict()
            else:
                params['drug_url'] = self.drug_url
        if self.frequency:
            if hasattr(self.frequency, 'to_alipay_dict'):
                params['frequency'] = self.frequency.to_alipay_dict()
            else:
                params['frequency'] = self.frequency
        if self.instructions:
            if hasattr(self.instructions, 'to_alipay_dict'):
                params['instructions'] = self.instructions.to_alipay_dict()
            else:
                params['instructions'] = self.instructions
        if self.medicine_quantity:
            if hasattr(self.medicine_quantity, 'to_alipay_dict'):
                params['medicine_quantity'] = self.medicine_quantity.to_alipay_dict()
            else:
                params['medicine_quantity'] = self.medicine_quantity
        if self.single_dose:
            if hasattr(self.single_dose, 'to_alipay_dict'):
                params['single_dose'] = self.single_dose.to_alipay_dict()
            else:
                params['single_dose'] = self.single_dose
        if self.spec:
            if hasattr(self.spec, 'to_alipay_dict'):
                params['spec'] = self.spec.to_alipay_dict()
            else:
                params['spec'] = self.spec
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PlatformPrescriptionDrugInfo()
        if 'administration_route' in d:
            o.administration_route = d['administration_route']
        if 'comments' in d:
            o.comments = d['comments']
        if 'dosage_form' in d:
            o.dosage_form = d['dosage_form']
        if 'drug_generic_name' in d:
            o.drug_generic_name = d['drug_generic_name']
        if 'drug_id' in d:
            o.drug_id = d['drug_id']
        if 'drug_name' in d:
            o.drug_name = d['drug_name']
        if 'drug_url' in d:
            o.drug_url = d['drug_url']
        if 'frequency' in d:
            o.frequency = d['frequency']
        if 'instructions' in d:
            o.instructions = d['instructions']
        if 'medicine_quantity' in d:
            o.medicine_quantity = d['medicine_quantity']
        if 'single_dose' in d:
            o.single_dose = d['single_dose']
        if 'spec' in d:
            o.spec = d['spec']
        return o


