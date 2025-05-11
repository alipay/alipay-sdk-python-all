#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MediaInfo import MediaInfo


class AlipayCommerceMedicalSupplierContentPublishModel(object):

    def __init__(self):
        self._author = None
        self._biz_content_id = None
        self._content = None
        self._media_info_list = None
        self._original_link = None
        self._owner_id = None
        self._owner_type = None
        self._permission_status = None
        self._publish_date = None
        self._source = None
        self._summary = None
        self._title = None
        self._type = None

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value
    @property
    def biz_content_id(self):
        return self._biz_content_id

    @biz_content_id.setter
    def biz_content_id(self, value):
        self._biz_content_id = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def media_info_list(self):
        return self._media_info_list

    @media_info_list.setter
    def media_info_list(self, value):
        if isinstance(value, list):
            self._media_info_list = list()
            for i in value:
                if isinstance(i, MediaInfo):
                    self._media_info_list.append(i)
                else:
                    self._media_info_list.append(MediaInfo.from_alipay_dict(i))
    @property
    def original_link(self):
        return self._original_link

    @original_link.setter
    def original_link(self, value):
        self._original_link = value
    @property
    def owner_id(self):
        return self._owner_id

    @owner_id.setter
    def owner_id(self, value):
        self._owner_id = value
    @property
    def owner_type(self):
        return self._owner_type

    @owner_type.setter
    def owner_type(self, value):
        self._owner_type = value
    @property
    def permission_status(self):
        return self._permission_status

    @permission_status.setter
    def permission_status(self, value):
        self._permission_status = value
    @property
    def publish_date(self):
        return self._publish_date

    @publish_date.setter
    def publish_date(self, value):
        self._publish_date = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def summary(self):
        return self._summary

    @summary.setter
    def summary(self, value):
        self._summary = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.author:
            if hasattr(self.author, 'to_alipay_dict'):
                params['author'] = self.author.to_alipay_dict()
            else:
                params['author'] = self.author
        if self.biz_content_id:
            if hasattr(self.biz_content_id, 'to_alipay_dict'):
                params['biz_content_id'] = self.biz_content_id.to_alipay_dict()
            else:
                params['biz_content_id'] = self.biz_content_id
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.media_info_list:
            if isinstance(self.media_info_list, list):
                for i in range(0, len(self.media_info_list)):
                    element = self.media_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.media_info_list[i] = element.to_alipay_dict()
            if hasattr(self.media_info_list, 'to_alipay_dict'):
                params['media_info_list'] = self.media_info_list.to_alipay_dict()
            else:
                params['media_info_list'] = self.media_info_list
        if self.original_link:
            if hasattr(self.original_link, 'to_alipay_dict'):
                params['original_link'] = self.original_link.to_alipay_dict()
            else:
                params['original_link'] = self.original_link
        if self.owner_id:
            if hasattr(self.owner_id, 'to_alipay_dict'):
                params['owner_id'] = self.owner_id.to_alipay_dict()
            else:
                params['owner_id'] = self.owner_id
        if self.owner_type:
            if hasattr(self.owner_type, 'to_alipay_dict'):
                params['owner_type'] = self.owner_type.to_alipay_dict()
            else:
                params['owner_type'] = self.owner_type
        if self.permission_status:
            if hasattr(self.permission_status, 'to_alipay_dict'):
                params['permission_status'] = self.permission_status.to_alipay_dict()
            else:
                params['permission_status'] = self.permission_status
        if self.publish_date:
            if hasattr(self.publish_date, 'to_alipay_dict'):
                params['publish_date'] = self.publish_date.to_alipay_dict()
            else:
                params['publish_date'] = self.publish_date
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.summary:
            if hasattr(self.summary, 'to_alipay_dict'):
                params['summary'] = self.summary.to_alipay_dict()
            else:
                params['summary'] = self.summary
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalSupplierContentPublishModel()
        if 'author' in d:
            o.author = d['author']
        if 'biz_content_id' in d:
            o.biz_content_id = d['biz_content_id']
        if 'content' in d:
            o.content = d['content']
        if 'media_info_list' in d:
            o.media_info_list = d['media_info_list']
        if 'original_link' in d:
            o.original_link = d['original_link']
        if 'owner_id' in d:
            o.owner_id = d['owner_id']
        if 'owner_type' in d:
            o.owner_type = d['owner_type']
        if 'permission_status' in d:
            o.permission_status = d['permission_status']
        if 'publish_date' in d:
            o.publish_date = d['publish_date']
        if 'source' in d:
            o.source = d['source']
        if 'summary' in d:
            o.summary = d['summary']
        if 'title' in d:
            o.title = d['title']
        if 'type' in d:
            o.type = d['type']
        return o


