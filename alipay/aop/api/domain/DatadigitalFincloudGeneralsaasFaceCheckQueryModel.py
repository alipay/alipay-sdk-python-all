#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalFincloudGeneralsaasFaceCheckQueryModel(object):

    def __init__(self):
        self._certify_id = None
        self._need_alive_photo = None
        self._need_attack_result = None
        self._need_quality_score = None
        self._need_score = None

    @property
    def certify_id(self):
        return self._certify_id

    @certify_id.setter
    def certify_id(self, value):
        self._certify_id = value
    @property
    def need_alive_photo(self):
        return self._need_alive_photo

    @need_alive_photo.setter
    def need_alive_photo(self, value):
        self._need_alive_photo = value
    @property
    def need_attack_result(self):
        return self._need_attack_result

    @need_attack_result.setter
    def need_attack_result(self, value):
        self._need_attack_result = value
    @property
    def need_quality_score(self):
        return self._need_quality_score

    @need_quality_score.setter
    def need_quality_score(self, value):
        self._need_quality_score = value
    @property
    def need_score(self):
        return self._need_score

    @need_score.setter
    def need_score(self, value):
        self._need_score = value


    def to_alipay_dict(self):
        params = dict()
        if self.certify_id:
            if hasattr(self.certify_id, 'to_alipay_dict'):
                params['certify_id'] = self.certify_id.to_alipay_dict()
            else:
                params['certify_id'] = self.certify_id
        if self.need_alive_photo:
            if hasattr(self.need_alive_photo, 'to_alipay_dict'):
                params['need_alive_photo'] = self.need_alive_photo.to_alipay_dict()
            else:
                params['need_alive_photo'] = self.need_alive_photo
        if self.need_attack_result:
            if hasattr(self.need_attack_result, 'to_alipay_dict'):
                params['need_attack_result'] = self.need_attack_result.to_alipay_dict()
            else:
                params['need_attack_result'] = self.need_attack_result
        if self.need_quality_score:
            if hasattr(self.need_quality_score, 'to_alipay_dict'):
                params['need_quality_score'] = self.need_quality_score.to_alipay_dict()
            else:
                params['need_quality_score'] = self.need_quality_score
        if self.need_score:
            if hasattr(self.need_score, 'to_alipay_dict'):
                params['need_score'] = self.need_score.to_alipay_dict()
            else:
                params['need_score'] = self.need_score
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalFincloudGeneralsaasFaceCheckQueryModel()
        if 'certify_id' in d:
            o.certify_id = d['certify_id']
        if 'need_alive_photo' in d:
            o.need_alive_photo = d['need_alive_photo']
        if 'need_attack_result' in d:
            o.need_attack_result = d['need_attack_result']
        if 'need_quality_score' in d:
            o.need_quality_score = d['need_quality_score']
        if 'need_score' in d:
            o.need_score = d['need_score']
        return o


