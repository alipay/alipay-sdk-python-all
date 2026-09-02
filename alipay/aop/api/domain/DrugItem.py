#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DrugItem(object):

    def __init__(self):
        self._drug_notice = None
        self._drugdosage = None
        self._drugduration = None
        self._drugfrequency = None
        self._drugname = None
        self._drugquantity = None
        self._drugspecification = None
        self._druguse = None

    @property
    def drug_notice(self):
        return self._drug_notice

    @drug_notice.setter
    def drug_notice(self, value):
        self._drug_notice = value
    @property
    def drugdosage(self):
        return self._drugdosage

    @drugdosage.setter
    def drugdosage(self, value):
        self._drugdosage = value
    @property
    def drugduration(self):
        return self._drugduration

    @drugduration.setter
    def drugduration(self, value):
        self._drugduration = value
    @property
    def drugfrequency(self):
        return self._drugfrequency

    @drugfrequency.setter
    def drugfrequency(self, value):
        self._drugfrequency = value
    @property
    def drugname(self):
        return self._drugname

    @drugname.setter
    def drugname(self, value):
        self._drugname = value
    @property
    def drugquantity(self):
        return self._drugquantity

    @drugquantity.setter
    def drugquantity(self, value):
        self._drugquantity = value
    @property
    def drugspecification(self):
        return self._drugspecification

    @drugspecification.setter
    def drugspecification(self, value):
        self._drugspecification = value
    @property
    def druguse(self):
        return self._druguse

    @druguse.setter
    def druguse(self, value):
        self._druguse = value


    def to_alipay_dict(self):
        params = dict()
        if self.drug_notice:
            if hasattr(self.drug_notice, 'to_alipay_dict'):
                params['drug_notice'] = self.drug_notice.to_alipay_dict()
            else:
                params['drug_notice'] = self.drug_notice
        if self.drugdosage:
            if hasattr(self.drugdosage, 'to_alipay_dict'):
                params['drugdosage'] = self.drugdosage.to_alipay_dict()
            else:
                params['drugdosage'] = self.drugdosage
        if self.drugduration:
            if hasattr(self.drugduration, 'to_alipay_dict'):
                params['drugduration'] = self.drugduration.to_alipay_dict()
            else:
                params['drugduration'] = self.drugduration
        if self.drugfrequency:
            if hasattr(self.drugfrequency, 'to_alipay_dict'):
                params['drugfrequency'] = self.drugfrequency.to_alipay_dict()
            else:
                params['drugfrequency'] = self.drugfrequency
        if self.drugname:
            if hasattr(self.drugname, 'to_alipay_dict'):
                params['drugname'] = self.drugname.to_alipay_dict()
            else:
                params['drugname'] = self.drugname
        if self.drugquantity:
            if hasattr(self.drugquantity, 'to_alipay_dict'):
                params['drugquantity'] = self.drugquantity.to_alipay_dict()
            else:
                params['drugquantity'] = self.drugquantity
        if self.drugspecification:
            if hasattr(self.drugspecification, 'to_alipay_dict'):
                params['drugspecification'] = self.drugspecification.to_alipay_dict()
            else:
                params['drugspecification'] = self.drugspecification
        if self.druguse:
            if hasattr(self.druguse, 'to_alipay_dict'):
                params['druguse'] = self.druguse.to_alipay_dict()
            else:
                params['druguse'] = self.druguse
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DrugItem()
        if 'drug_notice' in d:
            o.drug_notice = d['drug_notice']
        if 'drugdosage' in d:
            o.drugdosage = d['drugdosage']
        if 'drugduration' in d:
            o.drugduration = d['drugduration']
        if 'drugfrequency' in d:
            o.drugfrequency = d['drugfrequency']
        if 'drugname' in d:
            o.drugname = d['drugname']
        if 'drugquantity' in d:
            o.drugquantity = d['drugquantity']
        if 'drugspecification' in d:
            o.drugspecification = d['drugspecification']
        if 'druguse' in d:
            o.druguse = d['druguse']
        return o


