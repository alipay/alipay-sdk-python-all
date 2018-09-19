#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BillInferenceResult(object):

    def __init__(self):
        self._angle = None
        self._bill_score = None
        self._bill_version = None
        self._capital_sum = None
        self._date = None
        self._name = None
        self._no = None
        self._rotate_shape = None
        self._title = None

    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, value):
        self._angle = value
    @property
    def bill_score(self):
        return self._bill_score

    @bill_score.setter
    def bill_score(self, value):
        self._bill_score = value
    @property
    def bill_version(self):
        return self._bill_version

    @bill_version.setter
    def bill_version(self, value):
        self._bill_version = value
    @property
    def capital_sum(self):
        return self._capital_sum

    @capital_sum.setter
    def capital_sum(self, value):
        if isinstance(value, list):
            self._capital_sum = list()
            for i in value:
                self._capital_sum.append(i)
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if isinstance(value, list):
            self._date = list()
            for i in value:
                self._date.append(i)
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, list):
            self._name = list()
            for i in value:
                self._name.append(i)
    @property
    def no(self):
        return self._no

    @no.setter
    def no(self, value):
        if isinstance(value, list):
            self._no = list()
            for i in value:
                self._no.append(i)
    @property
    def rotate_shape(self):
        return self._rotate_shape

    @rotate_shape.setter
    def rotate_shape(self, value):
        if isinstance(value, list):
            self._rotate_shape = list()
            for i in value:
                self._rotate_shape.append(i)
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, list):
            self._title = list()
            for i in value:
                self._title.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.angle:
            if hasattr(self.angle, 'to_alipay_dict'):
                params['angle'] = self.angle.to_alipay_dict()
            else:
                params['angle'] = self.angle
        if self.bill_score:
            if hasattr(self.bill_score, 'to_alipay_dict'):
                params['bill_score'] = self.bill_score.to_alipay_dict()
            else:
                params['bill_score'] = self.bill_score
        if self.bill_version:
            if hasattr(self.bill_version, 'to_alipay_dict'):
                params['bill_version'] = self.bill_version.to_alipay_dict()
            else:
                params['bill_version'] = self.bill_version
        if self.capital_sum:
            if isinstance(self.capital_sum, list):
                for i in range(0, len(self.capital_sum)):
                    element = self.capital_sum[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.capital_sum[i] = element.to_alipay_dict()
            if hasattr(self.capital_sum, 'to_alipay_dict'):
                params['capital_sum'] = self.capital_sum.to_alipay_dict()
            else:
                params['capital_sum'] = self.capital_sum
        if self.date:
            if isinstance(self.date, list):
                for i in range(0, len(self.date)):
                    element = self.date[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.date[i] = element.to_alipay_dict()
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.name:
            if isinstance(self.name, list):
                for i in range(0, len(self.name)):
                    element = self.name[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.name[i] = element.to_alipay_dict()
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.no:
            if isinstance(self.no, list):
                for i in range(0, len(self.no)):
                    element = self.no[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.no[i] = element.to_alipay_dict()
            if hasattr(self.no, 'to_alipay_dict'):
                params['no'] = self.no.to_alipay_dict()
            else:
                params['no'] = self.no
        if self.rotate_shape:
            if isinstance(self.rotate_shape, list):
                for i in range(0, len(self.rotate_shape)):
                    element = self.rotate_shape[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.rotate_shape[i] = element.to_alipay_dict()
            if hasattr(self.rotate_shape, 'to_alipay_dict'):
                params['rotate_shape'] = self.rotate_shape.to_alipay_dict()
            else:
                params['rotate_shape'] = self.rotate_shape
        if self.title:
            if isinstance(self.title, list):
                for i in range(0, len(self.title)):
                    element = self.title[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.title[i] = element.to_alipay_dict()
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BillInferenceResult()
        if 'angle' in d:
            o.angle = d['angle']
        if 'bill_score' in d:
            o.bill_score = d['bill_score']
        if 'bill_version' in d:
            o.bill_version = d['bill_version']
        if 'capital_sum' in d:
            o.capital_sum = d['capital_sum']
        if 'date' in d:
            o.date = d['date']
        if 'name' in d:
            o.name = d['name']
        if 'no' in d:
            o.no = d['no']
        if 'rotate_shape' in d:
            o.rotate_shape = d['rotate_shape']
        if 'title' in d:
            o.title = d['title']
        return o


