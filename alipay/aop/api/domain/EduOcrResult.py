#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EduOcrResult(object):

    def __init__(self):
        self._edu_level = None
        self._graduate_conclusion = None
        self._major = None

    @property
    def edu_level(self):
        return self._edu_level

    @edu_level.setter
    def edu_level(self, value):
        self._edu_level = value
    @property
    def graduate_conclusion(self):
        return self._graduate_conclusion

    @graduate_conclusion.setter
    def graduate_conclusion(self, value):
        self._graduate_conclusion = value
    @property
    def major(self):
        return self._major

    @major.setter
    def major(self, value):
        self._major = value


    def to_alipay_dict(self):
        params = dict()
        if self.edu_level:
            if hasattr(self.edu_level, 'to_alipay_dict'):
                params['edu_level'] = self.edu_level.to_alipay_dict()
            else:
                params['edu_level'] = self.edu_level
        if self.graduate_conclusion:
            if hasattr(self.graduate_conclusion, 'to_alipay_dict'):
                params['graduate_conclusion'] = self.graduate_conclusion.to_alipay_dict()
            else:
                params['graduate_conclusion'] = self.graduate_conclusion
        if self.major:
            if hasattr(self.major, 'to_alipay_dict'):
                params['major'] = self.major.to_alipay_dict()
            else:
                params['major'] = self.major
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EduOcrResult()
        if 'edu_level' in d:
            o.edu_level = d['edu_level']
        if 'graduate_conclusion' in d:
            o.graduate_conclusion = d['graduate_conclusion']
        if 'major' in d:
            o.major = d['major']
        return o


