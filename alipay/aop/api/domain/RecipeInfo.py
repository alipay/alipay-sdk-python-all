#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DrugItem import DrugItem


class RecipeInfo(object):

    def __init__(self):
        self._diagnosis = None
        self._doc_notice = None
        self._druglist = None
        self._patientage = None
        self._patientsex = None
        self._patientweight = None
        self._prescription_id = None
        self._recipe_status = None
        self._recipe_time = None
        self._recipedrugtype = None
        self._refusemodifyreason = None

    @property
    def diagnosis(self):
        return self._diagnosis

    @diagnosis.setter
    def diagnosis(self, value):
        self._diagnosis = value
    @property
    def doc_notice(self):
        return self._doc_notice

    @doc_notice.setter
    def doc_notice(self, value):
        self._doc_notice = value
    @property
    def druglist(self):
        return self._druglist

    @druglist.setter
    def druglist(self, value):
        if isinstance(value, list):
            self._druglist = list()
            for i in value:
                if isinstance(i, DrugItem):
                    self._druglist.append(i)
                else:
                    self._druglist.append(DrugItem.from_alipay_dict(i))
    @property
    def patientage(self):
        return self._patientage

    @patientage.setter
    def patientage(self, value):
        self._patientage = value
    @property
    def patientsex(self):
        return self._patientsex

    @patientsex.setter
    def patientsex(self, value):
        self._patientsex = value
    @property
    def patientweight(self):
        return self._patientweight

    @patientweight.setter
    def patientweight(self, value):
        self._patientweight = value
    @property
    def prescription_id(self):
        return self._prescription_id

    @prescription_id.setter
    def prescription_id(self, value):
        self._prescription_id = value
    @property
    def recipe_status(self):
        return self._recipe_status

    @recipe_status.setter
    def recipe_status(self, value):
        self._recipe_status = value
    @property
    def recipe_time(self):
        return self._recipe_time

    @recipe_time.setter
    def recipe_time(self, value):
        self._recipe_time = value
    @property
    def recipedrugtype(self):
        return self._recipedrugtype

    @recipedrugtype.setter
    def recipedrugtype(self, value):
        self._recipedrugtype = value
    @property
    def refusemodifyreason(self):
        return self._refusemodifyreason

    @refusemodifyreason.setter
    def refusemodifyreason(self, value):
        self._refusemodifyreason = value


    def to_alipay_dict(self):
        params = dict()
        if self.diagnosis:
            if hasattr(self.diagnosis, 'to_alipay_dict'):
                params['diagnosis'] = self.diagnosis.to_alipay_dict()
            else:
                params['diagnosis'] = self.diagnosis
        if self.doc_notice:
            if hasattr(self.doc_notice, 'to_alipay_dict'):
                params['doc_notice'] = self.doc_notice.to_alipay_dict()
            else:
                params['doc_notice'] = self.doc_notice
        if self.druglist:
            if isinstance(self.druglist, list):
                for i in range(0, len(self.druglist)):
                    element = self.druglist[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.druglist[i] = element.to_alipay_dict()
            if hasattr(self.druglist, 'to_alipay_dict'):
                params['druglist'] = self.druglist.to_alipay_dict()
            else:
                params['druglist'] = self.druglist
        if self.patientage:
            if hasattr(self.patientage, 'to_alipay_dict'):
                params['patientage'] = self.patientage.to_alipay_dict()
            else:
                params['patientage'] = self.patientage
        if self.patientsex:
            if hasattr(self.patientsex, 'to_alipay_dict'):
                params['patientsex'] = self.patientsex.to_alipay_dict()
            else:
                params['patientsex'] = self.patientsex
        if self.patientweight:
            if hasattr(self.patientweight, 'to_alipay_dict'):
                params['patientweight'] = self.patientweight.to_alipay_dict()
            else:
                params['patientweight'] = self.patientweight
        if self.prescription_id:
            if hasattr(self.prescription_id, 'to_alipay_dict'):
                params['prescription_id'] = self.prescription_id.to_alipay_dict()
            else:
                params['prescription_id'] = self.prescription_id
        if self.recipe_status:
            if hasattr(self.recipe_status, 'to_alipay_dict'):
                params['recipe_status'] = self.recipe_status.to_alipay_dict()
            else:
                params['recipe_status'] = self.recipe_status
        if self.recipe_time:
            if hasattr(self.recipe_time, 'to_alipay_dict'):
                params['recipe_time'] = self.recipe_time.to_alipay_dict()
            else:
                params['recipe_time'] = self.recipe_time
        if self.recipedrugtype:
            if hasattr(self.recipedrugtype, 'to_alipay_dict'):
                params['recipedrugtype'] = self.recipedrugtype.to_alipay_dict()
            else:
                params['recipedrugtype'] = self.recipedrugtype
        if self.refusemodifyreason:
            if hasattr(self.refusemodifyreason, 'to_alipay_dict'):
                params['refusemodifyreason'] = self.refusemodifyreason.to_alipay_dict()
            else:
                params['refusemodifyreason'] = self.refusemodifyreason
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecipeInfo()
        if 'diagnosis' in d:
            o.diagnosis = d['diagnosis']
        if 'doc_notice' in d:
            o.doc_notice = d['doc_notice']
        if 'druglist' in d:
            o.druglist = d['druglist']
        if 'patientage' in d:
            o.patientage = d['patientage']
        if 'patientsex' in d:
            o.patientsex = d['patientsex']
        if 'patientweight' in d:
            o.patientweight = d['patientweight']
        if 'prescription_id' in d:
            o.prescription_id = d['prescription_id']
        if 'recipe_status' in d:
            o.recipe_status = d['recipe_status']
        if 'recipe_time' in d:
            o.recipe_time = d['recipe_time']
        if 'recipedrugtype' in d:
            o.recipedrugtype = d['recipedrugtype']
        if 'refusemodifyreason' in d:
            o.refusemodifyreason = d['refusemodifyreason']
        return o


