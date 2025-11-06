#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FamilyHistory(object):

    def __init__(self):
        self._disease_name = None
        self._family_relationship = None

    @property
    def disease_name(self):
        return self._disease_name

    @disease_name.setter
    def disease_name(self, value):
        self._disease_name = value
    @property
    def family_relationship(self):
        return self._family_relationship

    @family_relationship.setter
    def family_relationship(self, value):
        self._family_relationship = value


    def to_alipay_dict(self):
        params = dict()
        if self.disease_name:
            if hasattr(self.disease_name, 'to_alipay_dict'):
                params['disease_name'] = self.disease_name.to_alipay_dict()
            else:
                params['disease_name'] = self.disease_name
        if self.family_relationship:
            if hasattr(self.family_relationship, 'to_alipay_dict'):
                params['family_relationship'] = self.family_relationship.to_alipay_dict()
            else:
                params['family_relationship'] = self.family_relationship
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FamilyHistory()
        if 'disease_name' in d:
            o.disease_name = d['disease_name']
        if 'family_relationship' in d:
            o.family_relationship = d['family_relationship']
        return o


