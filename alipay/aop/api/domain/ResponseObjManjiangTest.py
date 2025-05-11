#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ResponseObjManjiangTest(object):

    def __init__(self):
        self._repsponse_id_json = None

    @property
    def repsponse_id_json(self):
        return self._repsponse_id_json

    @repsponse_id_json.setter
    def repsponse_id_json(self, value):
        self._repsponse_id_json = value


    def to_alipay_dict(self):
        params = dict()
        if self.repsponse_id_json:
            if hasattr(self.repsponse_id_json, 'to_alipay_dict'):
                params['repsponse_id_json'] = self.repsponse_id_json.to_alipay_dict()
            else:
                params['repsponse_id_json'] = self.repsponse_id_json
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ResponseObjManjiangTest()
        if 'repsponse_id_json' in d:
            o.repsponse_id_json = d['repsponse_id_json']
        return o


