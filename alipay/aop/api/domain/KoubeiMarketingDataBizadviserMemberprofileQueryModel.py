#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMarketingDataBizadviserMemberprofileQueryModel(object):

    def __init__(self):
        self._member_grade = None

    @property
    def member_grade(self):
        return self._member_grade

    @member_grade.setter
    def member_grade(self, value):
        self._member_grade = value


    def to_alipay_dict(self):
        params = dict()
        if self.member_grade:
            if hasattr(self.member_grade, 'to_alipay_dict'):
                params['member_grade'] = self.member_grade.to_alipay_dict()
            else:
                params['member_grade'] = self.member_grade
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMarketingDataBizadviserMemberprofileQueryModel()
        if 'member_grade' in d:
            o.member_grade = d['member_grade']
        return o


