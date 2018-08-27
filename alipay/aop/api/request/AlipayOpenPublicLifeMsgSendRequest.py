#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.ParamConstants import *




class AlipayOpenPublicLifeMsgSendRequest(object):

    def __init__(self, biz_model=None):
        self._biz_model = biz_model
        self._category = None
        self._content = None
        self._desc = None
        self._msg_type = None
        self._source_ext_info = None
        self._title = None
        self._unique_msg_id = None
        self._video_length = None
        self._video_samples = None
        self._video_size = None
        self._video_source = None
        self._video_temporary_url = None
        self._video_url = None
        self._cover = None
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
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def msg_type(self):
        return self._msg_type

    @msg_type.setter
    def msg_type(self, value):
        self._msg_type = value
    @property
    def source_ext_info(self):
        return self._source_ext_info

    @source_ext_info.setter
    def source_ext_info(self, value):
        self._source_ext_info = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def unique_msg_id(self):
        return self._unique_msg_id

    @unique_msg_id.setter
    def unique_msg_id(self, value):
        self._unique_msg_id = value
    @property
    def video_length(self):
        return self._video_length

    @video_length.setter
    def video_length(self, value):
        self._video_length = value
    @property
    def video_samples(self):
        return self._video_samples

    @video_samples.setter
    def video_samples(self, value):
        if isinstance(value, list):
            self._video_samples = list()
            for i in value:
                self._video_samples.append(i)
    @property
    def video_size(self):
        return self._video_size

    @video_size.setter
    def video_size(self, value):
        self._video_size = value
    @property
    def video_source(self):
        return self._video_source

    @video_source.setter
    def video_source(self, value):
        self._video_source = value
    @property
    def video_temporary_url(self):
        return self._video_temporary_url

    @video_temporary_url.setter
    def video_temporary_url(self, value):
        self._video_temporary_url = value
    @property
    def video_url(self):
        return self._video_url

    @video_url.setter
    def video_url(self, value):
        self._video_url = value

    @property
    def cover(self):
        return self._cover

    @cover.setter
    def cover(self, value):
        if not isinstance(value, FileItem):
            return
        self._cover = value

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
        params[P_METHOD] = 'alipay.open.public.life.msg.send'
        params[P_VERSION] = self.version
        if self.biz_model:
            params[P_BIZ_CONTENT] = json.dumps(obj=self.biz_model.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.category:
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = json.dumps(obj=self.category.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['category'] = self.category
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = json.dumps(obj=self.content.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['content'] = self.content
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = json.dumps(obj=self.desc.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['desc'] = self.desc
        if self.msg_type:
            if hasattr(self.msg_type, 'to_alipay_dict'):
                params['msg_type'] = json.dumps(obj=self.msg_type.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['msg_type'] = self.msg_type
        if self.source_ext_info:
            if hasattr(self.source_ext_info, 'to_alipay_dict'):
                params['source_ext_info'] = json.dumps(obj=self.source_ext_info.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['source_ext_info'] = self.source_ext_info
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = json.dumps(obj=self.title.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['title'] = self.title
        if self.unique_msg_id:
            if hasattr(self.unique_msg_id, 'to_alipay_dict'):
                params['unique_msg_id'] = json.dumps(obj=self.unique_msg_id.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['unique_msg_id'] = self.unique_msg_id
        if self.video_length:
            if hasattr(self.video_length, 'to_alipay_dict'):
                params['video_length'] = json.dumps(obj=self.video_length.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['video_length'] = self.video_length
        if self.video_samples:
            if isinstance(self.video_samples, list):
                for i in range(0, len(self.video_samples)):
                    element = self.video_samples[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.video_samples[i] = element.to_alipay_dict()
                params['video_samples'] = json.dumps(obj=self.video_samples, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.video_size:
            if hasattr(self.video_size, 'to_alipay_dict'):
                params['video_size'] = json.dumps(obj=self.video_size.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['video_size'] = self.video_size
        if self.video_source:
            if hasattr(self.video_source, 'to_alipay_dict'):
                params['video_source'] = json.dumps(obj=self.video_source.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['video_source'] = self.video_source
        if self.video_temporary_url:
            if hasattr(self.video_temporary_url, 'to_alipay_dict'):
                params['video_temporary_url'] = json.dumps(obj=self.video_temporary_url.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['video_temporary_url'] = self.video_temporary_url
        if self.video_url:
            if hasattr(self.video_url, 'to_alipay_dict'):
                params['video_url'] = json.dumps(obj=self.video_url.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['video_url'] = self.video_url
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
        if self.cover:
            multipart_params['cover'] = self.cover
        return multipart_params
