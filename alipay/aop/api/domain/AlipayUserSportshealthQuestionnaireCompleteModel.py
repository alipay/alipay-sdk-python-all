#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserSportshealthQuestionnaireCompleteModel(object):

    def __init__(self):
        self._biz_no = None
        self._open_id = None
        self._survey_result = None
        self._survey_type = None
        self._user_id = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def survey_result(self):
        return self._survey_result

    @survey_result.setter
    def survey_result(self, value):
        self._survey_result = value
    @property
    def survey_type(self):
        return self._survey_type

    @survey_type.setter
    def survey_type(self, value):
        self._survey_type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.survey_result:
            if hasattr(self.survey_result, 'to_alipay_dict'):
                params['survey_result'] = self.survey_result.to_alipay_dict()
            else:
                params['survey_result'] = self.survey_result
        if self.survey_type:
            if hasattr(self.survey_type, 'to_alipay_dict'):
                params['survey_type'] = self.survey_type.to_alipay_dict()
            else:
                params['survey_type'] = self.survey_type
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
        o = AlipayUserSportshealthQuestionnaireCompleteModel()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'survey_result' in d:
            o.survey_result = d['survey_result']
        if 'survey_type' in d:
            o.survey_type = d['survey_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


