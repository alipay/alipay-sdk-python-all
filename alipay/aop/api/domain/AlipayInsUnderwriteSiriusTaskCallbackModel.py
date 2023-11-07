#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsUnderwriteSiriusTaskCallbackModel(object):

    def __init__(self):
        self._biz_id = None
        self._ch_info = None
        self._channel_code = None
        self._code = None
        self._ext = None
        self._file_id = None
        self._load_test = None
        self._log_file_id = None
        self._message = None
        self._mode_code = None
        self._msg = None
        self._op_token = None
        self._payload = None
        self._payload_template_std_content = None
        self._retry_times = None
        self._scene_code = None
        self._sirius_app_id = None
        self._sirius_code = None
        self._sirius_env = None
        self._sirius_source = None
        self._site_user_id = None
        self._source_file_id = None
        self._task_payload = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def ch_info(self):
        return self._ch_info

    @ch_info.setter
    def ch_info(self, value):
        self._ch_info = value
    @property
    def channel_code(self):
        return self._channel_code

    @channel_code.setter
    def channel_code(self, value):
        self._channel_code = value
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def ext(self):
        return self._ext

    @ext.setter
    def ext(self, value):
        self._ext = value
    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value
    @property
    def load_test(self):
        return self._load_test

    @load_test.setter
    def load_test(self, value):
        self._load_test = value
    @property
    def log_file_id(self):
        return self._log_file_id

    @log_file_id.setter
    def log_file_id(self, value):
        self._log_file_id = value
    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value
    @property
    def mode_code(self):
        return self._mode_code

    @mode_code.setter
    def mode_code(self, value):
        self._mode_code = value
    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value
    @property
    def op_token(self):
        return self._op_token

    @op_token.setter
    def op_token(self, value):
        self._op_token = value
    @property
    def payload(self):
        return self._payload

    @payload.setter
    def payload(self, value):
        self._payload = value
    @property
    def payload_template_std_content(self):
        return self._payload_template_std_content

    @payload_template_std_content.setter
    def payload_template_std_content(self, value):
        self._payload_template_std_content = value
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
    def sirius_code(self):
        return self._sirius_code

    @sirius_code.setter
    def sirius_code(self, value):
        self._sirius_code = value
    @property
    def sirius_env(self):
        return self._sirius_env

    @sirius_env.setter
    def sirius_env(self, value):
        self._sirius_env = value
    @property
    def sirius_source(self):
        return self._sirius_source

    @sirius_source.setter
    def sirius_source(self, value):
        self._sirius_source = value
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
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.ch_info:
            if hasattr(self.ch_info, 'to_alipay_dict'):
                params['ch_info'] = self.ch_info.to_alipay_dict()
            else:
                params['ch_info'] = self.ch_info
        if self.channel_code:
            if hasattr(self.channel_code, 'to_alipay_dict'):
                params['channel_code'] = self.channel_code.to_alipay_dict()
            else:
                params['channel_code'] = self.channel_code
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.ext:
            if hasattr(self.ext, 'to_alipay_dict'):
                params['ext'] = self.ext.to_alipay_dict()
            else:
                params['ext'] = self.ext
        if self.file_id:
            if hasattr(self.file_id, 'to_alipay_dict'):
                params['file_id'] = self.file_id.to_alipay_dict()
            else:
                params['file_id'] = self.file_id
        if self.load_test:
            if hasattr(self.load_test, 'to_alipay_dict'):
                params['load_test'] = self.load_test.to_alipay_dict()
            else:
                params['load_test'] = self.load_test
        if self.log_file_id:
            if hasattr(self.log_file_id, 'to_alipay_dict'):
                params['log_file_id'] = self.log_file_id.to_alipay_dict()
            else:
                params['log_file_id'] = self.log_file_id
        if self.message:
            if hasattr(self.message, 'to_alipay_dict'):
                params['message'] = self.message.to_alipay_dict()
            else:
                params['message'] = self.message
        if self.mode_code:
            if hasattr(self.mode_code, 'to_alipay_dict'):
                params['mode_code'] = self.mode_code.to_alipay_dict()
            else:
                params['mode_code'] = self.mode_code
        if self.msg:
            if hasattr(self.msg, 'to_alipay_dict'):
                params['msg'] = self.msg.to_alipay_dict()
            else:
                params['msg'] = self.msg
        if self.op_token:
            if hasattr(self.op_token, 'to_alipay_dict'):
                params['op_token'] = self.op_token.to_alipay_dict()
            else:
                params['op_token'] = self.op_token
        if self.payload:
            if hasattr(self.payload, 'to_alipay_dict'):
                params['payload'] = self.payload.to_alipay_dict()
            else:
                params['payload'] = self.payload
        if self.payload_template_std_content:
            if hasattr(self.payload_template_std_content, 'to_alipay_dict'):
                params['payload_template_std_content'] = self.payload_template_std_content.to_alipay_dict()
            else:
                params['payload_template_std_content'] = self.payload_template_std_content
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
        if self.sirius_code:
            if hasattr(self.sirius_code, 'to_alipay_dict'):
                params['sirius_code'] = self.sirius_code.to_alipay_dict()
            else:
                params['sirius_code'] = self.sirius_code
        if self.sirius_env:
            if hasattr(self.sirius_env, 'to_alipay_dict'):
                params['sirius_env'] = self.sirius_env.to_alipay_dict()
            else:
                params['sirius_env'] = self.sirius_env
        if self.sirius_source:
            if hasattr(self.sirius_source, 'to_alipay_dict'):
                params['sirius_source'] = self.sirius_source.to_alipay_dict()
            else:
                params['sirius_source'] = self.sirius_source
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
        o = AlipayInsUnderwriteSiriusTaskCallbackModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'ch_info' in d:
            o.ch_info = d['ch_info']
        if 'channel_code' in d:
            o.channel_code = d['channel_code']
        if 'code' in d:
            o.code = d['code']
        if 'ext' in d:
            o.ext = d['ext']
        if 'file_id' in d:
            o.file_id = d['file_id']
        if 'load_test' in d:
            o.load_test = d['load_test']
        if 'log_file_id' in d:
            o.log_file_id = d['log_file_id']
        if 'message' in d:
            o.message = d['message']
        if 'mode_code' in d:
            o.mode_code = d['mode_code']
        if 'msg' in d:
            o.msg = d['msg']
        if 'op_token' in d:
            o.op_token = d['op_token']
        if 'payload' in d:
            o.payload = d['payload']
        if 'payload_template_std_content' in d:
            o.payload_template_std_content = d['payload_template_std_content']
        if 'retry_times' in d:
            o.retry_times = d['retry_times']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'sirius_app_id' in d:
            o.sirius_app_id = d['sirius_app_id']
        if 'sirius_code' in d:
            o.sirius_code = d['sirius_code']
        if 'sirius_env' in d:
            o.sirius_env = d['sirius_env']
        if 'sirius_source' in d:
            o.sirius_source = d['sirius_source']
        if 'site_user_id' in d:
            o.site_user_id = d['site_user_id']
        if 'source_file_id' in d:
            o.source_file_id = d['source_file_id']
        if 'task_payload' in d:
            o.task_payload = d['task_payload']
        return o


