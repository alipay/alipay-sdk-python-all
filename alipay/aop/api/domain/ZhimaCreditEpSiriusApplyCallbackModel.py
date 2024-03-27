#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpSiriusApplyCallbackModel(object):

    def __init__(self):
        self._apply_no = None
        self._apply_status = None
        self._biz_id = None
        self._channel_code = None
        self._encrypted = None
        self._file_id = None
        self._mode_code = None
        self._out_biz_no = None
        self._payload = None
        self._request_id = None
        self._retry_times = None
        self._scene_code = None
        self._sirius_app_id = None
        self._site_user_id = None
        self._source_file_id = None
        self._task_payload = None

    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def apply_status(self):
        return self._apply_status

    @apply_status.setter
    def apply_status(self, value):
        self._apply_status = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def channel_code(self):
        return self._channel_code

    @channel_code.setter
    def channel_code(self, value):
        self._channel_code = value
    @property
    def encrypted(self):
        return self._encrypted

    @encrypted.setter
    def encrypted(self, value):
        self._encrypted = value
    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value
    @property
    def mode_code(self):
        return self._mode_code

    @mode_code.setter
    def mode_code(self, value):
        self._mode_code = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def payload(self):
        return self._payload

    @payload.setter
    def payload(self, value):
        self._payload = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def retry_times(self):
        return self._retry_times

    @retry_times.setter
    def retry_times(self, value):
        self._retry_times = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def sirius_app_id(self):
        return self._sirius_app_id

    @sirius_app_id.setter
    def sirius_app_id(self, value):
        self._sirius_app_id = value
    @property
    def site_user_id(self):
        return self._site_user_id

    @site_user_id.setter
    def site_user_id(self, value):
        self._site_user_id = value
    @property
    def source_file_id(self):
        return self._source_file_id

    @source_file_id.setter
    def source_file_id(self, value):
        self._source_file_id = value
    @property
    def task_payload(self):
        return self._task_payload

    @task_payload.setter
    def task_payload(self, value):
        self._task_payload = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_no:
            if hasattr(self.apply_no, 'to_alipay_dict'):
                params['apply_no'] = self.apply_no.to_alipay_dict()
            else:
                params['apply_no'] = self.apply_no
        if self.apply_status:
            if hasattr(self.apply_status, 'to_alipay_dict'):
                params['apply_status'] = self.apply_status.to_alipay_dict()
            else:
                params['apply_status'] = self.apply_status
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.channel_code:
            if hasattr(self.channel_code, 'to_alipay_dict'):
                params['channel_code'] = self.channel_code.to_alipay_dict()
            else:
                params['channel_code'] = self.channel_code
        if self.encrypted:
            if hasattr(self.encrypted, 'to_alipay_dict'):
                params['encrypted'] = self.encrypted.to_alipay_dict()
            else:
                params['encrypted'] = self.encrypted
        if self.file_id:
            if hasattr(self.file_id, 'to_alipay_dict'):
                params['file_id'] = self.file_id.to_alipay_dict()
            else:
                params['file_id'] = self.file_id
        if self.mode_code:
            if hasattr(self.mode_code, 'to_alipay_dict'):
                params['mode_code'] = self.mode_code.to_alipay_dict()
            else:
                params['mode_code'] = self.mode_code
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.payload:
            if hasattr(self.payload, 'to_alipay_dict'):
                params['payload'] = self.payload.to_alipay_dict()
            else:
                params['payload'] = self.payload
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.retry_times:
            if hasattr(self.retry_times, 'to_alipay_dict'):
                params['retry_times'] = self.retry_times.to_alipay_dict()
            else:
                params['retry_times'] = self.retry_times
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.sirius_app_id:
            if hasattr(self.sirius_app_id, 'to_alipay_dict'):
                params['sirius_app_id'] = self.sirius_app_id.to_alipay_dict()
            else:
                params['sirius_app_id'] = self.sirius_app_id
        if self.site_user_id:
            if hasattr(self.site_user_id, 'to_alipay_dict'):
                params['site_user_id'] = self.site_user_id.to_alipay_dict()
            else:
                params['site_user_id'] = self.site_user_id
        if self.source_file_id:
            if hasattr(self.source_file_id, 'to_alipay_dict'):
                params['source_file_id'] = self.source_file_id.to_alipay_dict()
            else:
                params['source_file_id'] = self.source_file_id
        if self.task_payload:
            if hasattr(self.task_payload, 'to_alipay_dict'):
                params['task_payload'] = self.task_payload.to_alipay_dict()
            else:
                params['task_payload'] = self.task_payload
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpSiriusApplyCallbackModel()
        if 'apply_no' in d:
            o.apply_no = d['apply_no']
        if 'apply_status' in d:
            o.apply_status = d['apply_status']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'channel_code' in d:
            o.channel_code = d['channel_code']
        if 'encrypted' in d:
            o.encrypted = d['encrypted']
        if 'file_id' in d:
            o.file_id = d['file_id']
        if 'mode_code' in d:
            o.mode_code = d['mode_code']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'payload' in d:
            o.payload = d['payload']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'retry_times' in d:
            o.retry_times = d['retry_times']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'sirius_app_id' in d:
            o.sirius_app_id = d['sirius_app_id']
        if 'site_user_id' in d:
            o.site_user_id = d['site_user_id']
        if 'source_file_id' in d:
            o.source_file_id = d['source_file_id']
        if 'task_payload' in d:
            o.task_payload = d['task_payload']
        return o


