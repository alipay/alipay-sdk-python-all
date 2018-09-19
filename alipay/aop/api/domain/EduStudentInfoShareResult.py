#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.StudentInfo import StudentInfo


class EduStudentInfoShareResult(object):

    def __init__(self):
        self._biz_type = None
        self._student_infos = None
        self._user_id = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def student_infos(self):
        return self._student_infos

    @student_infos.setter
    def student_infos(self, value):
        if isinstance(value, list):
            self._student_infos = list()
            for i in value:
                if isinstance(i, StudentInfo):
                    self._student_infos.append(i)
                else:
                    self._student_infos.append(StudentInfo.from_alipay_dict(i))
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.student_infos:
            if isinstance(self.student_infos, list):
                for i in range(0, len(self.student_infos)):
                    element = self.student_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.student_infos[i] = element.to_alipay_dict()
            if hasattr(self.student_infos, 'to_alipay_dict'):
                params['student_infos'] = self.student_infos.to_alipay_dict()
            else:
                params['student_infos'] = self.student_infos
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EduStudentInfoShareResult()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'student_infos' in d:
            o.student_infos = d['student_infos']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


