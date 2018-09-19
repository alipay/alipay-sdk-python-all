#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BenefitGradeConfig(object):

    def __init__(self):
        self._background_url = None
        self._detail = None
        self._grade = None
        self._page_url = None
        self._point = None
        self._point_discount = None

    @property
    def background_url(self):
        return self._background_url

    @background_url.setter
    def background_url(self, value):
        self._background_url = value
    @property
    def detail(self):
        return self._detail

    @detail.setter
    def detail(self, value):
        self._detail = value
    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        self._grade = value
    @property
    def page_url(self):
        return self._page_url

    @page_url.setter
    def page_url(self, value):
        self._page_url = value
    @property
    def point(self):
        return self._point

    @point.setter
    def point(self, value):
        self._point = value
    @property
    def point_discount(self):
        return self._point_discount

    @point_discount.setter
    def point_discount(self, value):
        self._point_discount = value


    def to_alipay_dict(self):
        params = dict()
        if self.background_url:
            if hasattr(self.background_url, 'to_alipay_dict'):
                params['background_url'] = self.background_url.to_alipay_dict()
            else:
                params['background_url'] = self.background_url
        if self.detail:
            if hasattr(self.detail, 'to_alipay_dict'):
                params['detail'] = self.detail.to_alipay_dict()
            else:
                params['detail'] = self.detail
        if self.grade:
            if hasattr(self.grade, 'to_alipay_dict'):
                params['grade'] = self.grade.to_alipay_dict()
            else:
                params['grade'] = self.grade
        if self.page_url:
            if hasattr(self.page_url, 'to_alipay_dict'):
                params['page_url'] = self.page_url.to_alipay_dict()
            else:
                params['page_url'] = self.page_url
        if self.point:
            if hasattr(self.point, 'to_alipay_dict'):
                params['point'] = self.point.to_alipay_dict()
            else:
                params['point'] = self.point
        if self.point_discount:
            if hasattr(self.point_discount, 'to_alipay_dict'):
                params['point_discount'] = self.point_discount.to_alipay_dict()
            else:
                params['point_discount'] = self.point_discount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BenefitGradeConfig()
        if 'background_url' in d:
            o.background_url = d['background_url']
        if 'detail' in d:
            o.detail = d['detail']
        if 'grade' in d:
            o.grade = d['grade']
        if 'page_url' in d:
            o.page_url = d['page_url']
        if 'point' in d:
            o.point = d['point']
        if 'point_discount' in d:
            o.point_discount = d['point_discount']
        return o


