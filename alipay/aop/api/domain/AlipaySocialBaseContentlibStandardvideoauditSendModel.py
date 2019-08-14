#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialBaseContentlibStandardvideoauditSendModel(object):

    def __init__(self):
        self._action_type = None
        self._ext_info = None
        self._reason = None
        self._source_publish_date = None
        self._video_id = None
        self._video_length = None
        self._video_publish_type = None
        self._video_size = None
        self._video_tags = None
        self._video_url = None

    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value
    @property
    def source_publish_date(self):
        return self._source_publish_date

    @source_publish_date.setter
    def source_publish_date(self, value):
        self._source_publish_date = value
    @property
    def video_id(self):
        return self._video_id

    @video_id.setter
    def video_id(self, value):
        self._video_id = value
    @property
    def video_length(self):
        return self._video_length

    @video_length.setter
    def video_length(self, value):
        self._video_length = value
    @property
    def video_publish_type(self):
        return self._video_publish_type

    @video_publish_type.setter
    def video_publish_type(self, value):
        self._video_publish_type = value
    @property
    def video_size(self):
        return self._video_size

    @video_size.setter
    def video_size(self, value):
        self._video_size = value
    @property
    def video_tags(self):
        return self._video_tags

    @video_tags.setter
    def video_tags(self, value):
        self._video_tags = value
    @property
    def video_url(self):
        return self._video_url

    @video_url.setter
    def video_url(self, value):
        self._video_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_type:
            if hasattr(self.action_type, 'to_alipay_dict'):
                params['action_type'] = self.action_type.to_alipay_dict()
            else:
                params['action_type'] = self.action_type
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.reason:
            if hasattr(self.reason, 'to_alipay_dict'):
                params['reason'] = self.reason.to_alipay_dict()
            else:
                params['reason'] = self.reason
        if self.source_publish_date:
            if hasattr(self.source_publish_date, 'to_alipay_dict'):
                params['source_publish_date'] = self.source_publish_date.to_alipay_dict()
            else:
                params['source_publish_date'] = self.source_publish_date
        if self.video_id:
            if hasattr(self.video_id, 'to_alipay_dict'):
                params['video_id'] = self.video_id.to_alipay_dict()
            else:
                params['video_id'] = self.video_id
        if self.video_length:
            if hasattr(self.video_length, 'to_alipay_dict'):
                params['video_length'] = self.video_length.to_alipay_dict()
            else:
                params['video_length'] = self.video_length
        if self.video_publish_type:
            if hasattr(self.video_publish_type, 'to_alipay_dict'):
                params['video_publish_type'] = self.video_publish_type.to_alipay_dict()
            else:
                params['video_publish_type'] = self.video_publish_type
        if self.video_size:
            if hasattr(self.video_size, 'to_alipay_dict'):
                params['video_size'] = self.video_size.to_alipay_dict()
            else:
                params['video_size'] = self.video_size
        if self.video_tags:
            if hasattr(self.video_tags, 'to_alipay_dict'):
                params['video_tags'] = self.video_tags.to_alipay_dict()
            else:
                params['video_tags'] = self.video_tags
        if self.video_url:
            if hasattr(self.video_url, 'to_alipay_dict'):
                params['video_url'] = self.video_url.to_alipay_dict()
            else:
                params['video_url'] = self.video_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySocialBaseContentlibStandardvideoauditSendModel()
        if 'action_type' in d:
            o.action_type = d['action_type']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'reason' in d:
            o.reason = d['reason']
        if 'source_publish_date' in d:
            o.source_publish_date = d['source_publish_date']
        if 'video_id' in d:
            o.video_id = d['video_id']
        if 'video_length' in d:
            o.video_length = d['video_length']
        if 'video_publish_type' in d:
            o.video_publish_type = d['video_publish_type']
        if 'video_size' in d:
            o.video_size = d['video_size']
        if 'video_tags' in d:
            o.video_tags = d['video_tags']
        if 'video_url' in d:
            o.video_url = d['video_url']
        return o


