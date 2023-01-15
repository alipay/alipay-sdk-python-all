#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InteractiveServiceRecordDetail(object):

    def __init__(self):
        self._batch_biz_id = None
        self._biz_id = None
        self._commodity_id = None
        self._commodity_scene = None
        self._content_code = None
        self._dialogue = None
        self._download_url = None
        self._end_time = None
        self._interact_duration = None
        self._interact_result = None
        self._open_id = None
        self._phone_number = None
        self._product_code = None
        self._risk_labels = None
        self._risk_types = None
        self._start_time = None
        self._total_round = None
        self._user_id = None

    @property
    def batch_biz_id(self):
        return self._batch_biz_id

    @batch_biz_id.setter
    def batch_biz_id(self, value):
        self._batch_biz_id = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def commodity_id(self):
        return self._commodity_id

    @commodity_id.setter
    def commodity_id(self, value):
        self._commodity_id = value
    @property
    def commodity_scene(self):
        return self._commodity_scene

    @commodity_scene.setter
    def commodity_scene(self, value):
        self._commodity_scene = value
    @property
    def content_code(self):
        return self._content_code

    @content_code.setter
    def content_code(self, value):
        self._content_code = value
    @property
    def dialogue(self):
        return self._dialogue

    @dialogue.setter
    def dialogue(self, value):
        self._dialogue = value
    @property
    def download_url(self):
        return self._download_url

    @download_url.setter
    def download_url(self, value):
        self._download_url = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def interact_duration(self):
        return self._interact_duration

    @interact_duration.setter
    def interact_duration(self, value):
        self._interact_duration = value
    @property
    def interact_result(self):
        return self._interact_result

    @interact_result.setter
    def interact_result(self, value):
        self._interact_result = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def risk_labels(self):
        return self._risk_labels

    @risk_labels.setter
    def risk_labels(self, value):
        if isinstance(value, list):
            self._risk_labels = list()
            for i in value:
                self._risk_labels.append(i)
    @property
    def risk_types(self):
        return self._risk_types

    @risk_types.setter
    def risk_types(self, value):
        if isinstance(value, list):
            self._risk_types = list()
            for i in value:
                self._risk_types.append(i)
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def total_round(self):
        return self._total_round

    @total_round.setter
    def total_round(self, value):
        self._total_round = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_biz_id:
            if hasattr(self.batch_biz_id, 'to_alipay_dict'):
                params['batch_biz_id'] = self.batch_biz_id.to_alipay_dict()
            else:
                params['batch_biz_id'] = self.batch_biz_id
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.commodity_id:
            if hasattr(self.commodity_id, 'to_alipay_dict'):
                params['commodity_id'] = self.commodity_id.to_alipay_dict()
            else:
                params['commodity_id'] = self.commodity_id
        if self.commodity_scene:
            if hasattr(self.commodity_scene, 'to_alipay_dict'):
                params['commodity_scene'] = self.commodity_scene.to_alipay_dict()
            else:
                params['commodity_scene'] = self.commodity_scene
        if self.content_code:
            if hasattr(self.content_code, 'to_alipay_dict'):
                params['content_code'] = self.content_code.to_alipay_dict()
            else:
                params['content_code'] = self.content_code
        if self.dialogue:
            if hasattr(self.dialogue, 'to_alipay_dict'):
                params['dialogue'] = self.dialogue.to_alipay_dict()
            else:
                params['dialogue'] = self.dialogue
        if self.download_url:
            if hasattr(self.download_url, 'to_alipay_dict'):
                params['download_url'] = self.download_url.to_alipay_dict()
            else:
                params['download_url'] = self.download_url
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.interact_duration:
            if hasattr(self.interact_duration, 'to_alipay_dict'):
                params['interact_duration'] = self.interact_duration.to_alipay_dict()
            else:
                params['interact_duration'] = self.interact_duration
        if self.interact_result:
            if hasattr(self.interact_result, 'to_alipay_dict'):
                params['interact_result'] = self.interact_result.to_alipay_dict()
            else:
                params['interact_result'] = self.interact_result
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.phone_number:
            if hasattr(self.phone_number, 'to_alipay_dict'):
                params['phone_number'] = self.phone_number.to_alipay_dict()
            else:
                params['phone_number'] = self.phone_number
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.risk_labels:
            if isinstance(self.risk_labels, list):
                for i in range(0, len(self.risk_labels)):
                    element = self.risk_labels[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.risk_labels[i] = element.to_alipay_dict()
            if hasattr(self.risk_labels, 'to_alipay_dict'):
                params['risk_labels'] = self.risk_labels.to_alipay_dict()
            else:
                params['risk_labels'] = self.risk_labels
        if self.risk_types:
            if isinstance(self.risk_types, list):
                for i in range(0, len(self.risk_types)):
                    element = self.risk_types[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.risk_types[i] = element.to_alipay_dict()
            if hasattr(self.risk_types, 'to_alipay_dict'):
                params['risk_types'] = self.risk_types.to_alipay_dict()
            else:
                params['risk_types'] = self.risk_types
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.total_round:
            if hasattr(self.total_round, 'to_alipay_dict'):
                params['total_round'] = self.total_round.to_alipay_dict()
            else:
                params['total_round'] = self.total_round
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
        o = InteractiveServiceRecordDetail()
        if 'batch_biz_id' in d:
            o.batch_biz_id = d['batch_biz_id']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'commodity_id' in d:
            o.commodity_id = d['commodity_id']
        if 'commodity_scene' in d:
            o.commodity_scene = d['commodity_scene']
        if 'content_code' in d:
            o.content_code = d['content_code']
        if 'dialogue' in d:
            o.dialogue = d['dialogue']
        if 'download_url' in d:
            o.download_url = d['download_url']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'interact_duration' in d:
            o.interact_duration = d['interact_duration']
        if 'interact_result' in d:
            o.interact_result = d['interact_result']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'phone_number' in d:
            o.phone_number = d['phone_number']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'risk_labels' in d:
            o.risk_labels = d['risk_labels']
        if 'risk_types' in d:
            o.risk_types = d['risk_types']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'total_round' in d:
            o.total_round = d['total_round']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


