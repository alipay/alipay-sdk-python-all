#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.ParamConstants import *




class ZhimaCreditEpCodecCreateRequest(object):

    def __init__(self, biz_model=None):
        self._biz_model = biz_model
        self._channel_id = None
        self._channel_name = None
        self._goto_url = None
        self._subtitle = None
        self._title = None
        self._content_img = None
        self._logo_img = None
        self._version = "1.0"
        self._terminal_type = None
        self._terminal_info = None
        self._prod_code = None
        self._notify_url = None
        self._return_url = None
        self._udf_params = None
        self._need_encrypt = False

    @property
    def biz_model(self):
        return self._biz_model

    @biz_model.setter
    def biz_model(self, value):
        self._biz_model = value

    @property
    def channel_id(self):
        return self._channel_id

    @channel_id.setter
    def channel_id(self, value):
        self._channel_id = value
    @property
    def channel_name(self):
        return self._channel_name

    @channel_name.setter
    def channel_name(self, value):
        self._channel_name = value
    @property
    def goto_url(self):
        return self._goto_url

    @goto_url.setter
    def goto_url(self, value):
        self._goto_url = value
    @property
    def subtitle(self):
        return self._subtitle

    @subtitle.setter
    def subtitle(self, value):
        self._subtitle = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def content_img(self):
        return self._content_img

    @content_img.setter
    def content_img(self, value):
        if not isinstance(value, FileItem):
            return
        self._content_img = value
    @property
    def logo_img(self):
        return self._logo_img

    @logo_img.setter
    def logo_img(self, value):
        if not isinstance(value, FileItem):
            return
        self._logo_img = value

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, value):
        self._version = value

    @property
    def terminal_type(self):
        return self._terminal_type

    @terminal_type.setter
    def terminal_type(self, value):
        self._terminal_type = value

    @property
    def terminal_info(self):
        return self._terminal_info

    @terminal_info.setter
    def terminal_info(self, value):
        self._terminal_info = value

    @property
    def prod_code(self):
        return self._prod_code

    @prod_code.setter
    def prod_code(self, value):
        self._prod_code = value

    @property
    def notify_url(self):
        return self._notify_url

    @notify_url.setter
    def notify_url(self, value):
        self._notify_url = value

    @property
    def return_url(self):
        return self._return_url

    @return_url.setter
    def return_url(self, value):
        self._return_url = value

    @property
    def udf_params(self):
        return self._udf_params

    @udf_params.setter
    def udf_params(self, value):
        if not isinstance(value, dict):
            return
        self._udf_params = value

    @property
    def need_encrypt(self):
        return self._need_encrypt

    @need_encrypt.setter
    def need_encrypt(self, value):
        self._need_encrypt = value

    def add_other_text_param(self, key, value):
        if not self.udf_params:
            self.udf_params = dict()
        self.udf_params[key] = value

    def get_params(self):
        params = dict()
        params[P_METHOD] = 'zhima.credit.ep.codec.create'
        params[P_VERSION] = self.version
        if self.biz_model:
            params[P_BIZ_CONTENT] = json.dumps(obj=self.biz_model.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.channel_id:
            if hasattr(self.channel_id, 'to_alipay_dict'):
                params['channel_id'] = json.dumps(obj=self.channel_id.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['channel_id'] = self.channel_id
        if self.channel_name:
            if hasattr(self.channel_name, 'to_alipay_dict'):
                params['channel_name'] = json.dumps(obj=self.channel_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['channel_name'] = self.channel_name
        if self.goto_url:
            if hasattr(self.goto_url, 'to_alipay_dict'):
                params['goto_url'] = json.dumps(obj=self.goto_url.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['goto_url'] = self.goto_url
        if self.subtitle:
            if hasattr(self.subtitle, 'to_alipay_dict'):
                params['subtitle'] = json.dumps(obj=self.subtitle.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['subtitle'] = self.subtitle
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = json.dumps(obj=self.title.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['title'] = self.title
        if self.terminal_type:
            params['terminal_type'] = self.terminal_type
        if self.terminal_info:
            params['terminal_info'] = self.terminal_info
        if self.prod_code:
            params['prod_code'] = self.prod_code
        if self.notify_url:
            params['notify_url'] = self.notify_url
        if self.return_url:
            params['return_url'] = self.return_url
        if self.udf_params:
            params.update(self.udf_params)
        return params

    def get_multipart_params(self):
        multipart_params = dict()
        if self.content_img:
            multipart_params['content_img'] = self.content_img
        if self.logo_img:
            multipart_params['logo_img'] = self.logo_img
        return multipart_params
