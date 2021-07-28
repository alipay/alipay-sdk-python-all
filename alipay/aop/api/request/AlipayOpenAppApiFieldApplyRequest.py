#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.ParamConstants import *

from alipay.aop.api.domain.AuthFieldApply import AuthFieldApply



class AlipayOpenAppApiFieldApplyRequest(object):

    def __init__(self, biz_model=None):
        self._biz_model = biz_model
        self._auth_field_apply = None
        self._picture_1 = None
        self._picture_2 = None
        self._picture_3 = None
        self._picture_4 = None
        self._picture_5 = None
        self._video = None
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
    def auth_field_apply(self):
        return self._auth_field_apply

    @auth_field_apply.setter
    def auth_field_apply(self, value):
        if isinstance(value, AuthFieldApply):
            self._auth_field_apply = value
        else:
            self._auth_field_apply = AuthFieldApply.from_alipay_dict(value)

    @property
    def picture_1(self):
        return self._picture_1

    @picture_1.setter
    def picture_1(self, value):
        if not isinstance(value, FileItem):
            return
        self._picture_1 = value
    @property
    def picture_2(self):
        return self._picture_2

    @picture_2.setter
    def picture_2(self, value):
        if not isinstance(value, FileItem):
            return
        self._picture_2 = value
    @property
    def picture_3(self):
        return self._picture_3

    @picture_3.setter
    def picture_3(self, value):
        if not isinstance(value, FileItem):
            return
        self._picture_3 = value
    @property
    def picture_4(self):
        return self._picture_4

    @picture_4.setter
    def picture_4(self, value):
        if not isinstance(value, FileItem):
            return
        self._picture_4 = value
    @property
    def picture_5(self):
        return self._picture_5

    @picture_5.setter
    def picture_5(self, value):
        if not isinstance(value, FileItem):
            return
        self._picture_5 = value
    @property
    def video(self):
        return self._video

    @video.setter
    def video(self, value):
        if not isinstance(value, FileItem):
            return
        self._video = value

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
        params[P_METHOD] = 'alipay.open.app.api.field.apply'
        params[P_VERSION] = self.version
        if self.biz_model:
            params[P_BIZ_CONTENT] = json.dumps(obj=self.biz_model.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.auth_field_apply:
            if hasattr(self.auth_field_apply, 'to_alipay_dict'):
                params['auth_field_apply'] = json.dumps(obj=self.auth_field_apply.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['auth_field_apply'] = self.auth_field_apply
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
        if self.picture_1:
            multipart_params['picture_1'] = self.picture_1
        if self.picture_2:
            multipart_params['picture_2'] = self.picture_2
        if self.picture_3:
            multipart_params['picture_3'] = self.picture_3
        if self.picture_4:
            multipart_params['picture_4'] = self.picture_4
        if self.picture_5:
            multipart_params['picture_5'] = self.picture_5
        if self.video:
            multipart_params['video'] = self.video
        return multipart_params
