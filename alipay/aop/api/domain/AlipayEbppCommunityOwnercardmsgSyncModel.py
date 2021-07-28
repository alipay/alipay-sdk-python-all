#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppCommunityOwnercardmsgSyncModel(object):

    def __init__(self):
        self._biz_type = None
        self._city = None
        self._community = None
        self._community_short_name = None
        self._county = None
        self._expired_time = None
        self._id = None
        self._is_top = None
        self._link_url = None
        self._out_id = None
        self._province = None
        self._publish_time = None
        self._publisher = None
        self._service_type = None
        self._status = None
        self._street = None
        self._sub_biz_type = None
        self._template_content = None
        self._template_type = None
        self._title = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def community(self):
        return self._community

    @community.setter
    def community(self, value):
        self._community = value
    @property
    def community_short_name(self):
        return self._community_short_name

    @community_short_name.setter
    def community_short_name(self, value):
        self._community_short_name = value
    @property
    def county(self):
        return self._county

    @county.setter
    def county(self, value):
        self._county = value
    @property
    def expired_time(self):
        return self._expired_time

    @expired_time.setter
    def expired_time(self, value):
        self._expired_time = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def is_top(self):
        return self._is_top

    @is_top.setter
    def is_top(self, value):
        self._is_top = value
    @property
    def link_url(self):
        return self._link_url

    @link_url.setter
    def link_url(self, value):
        self._link_url = value
    @property
    def out_id(self):
        return self._out_id

    @out_id.setter
    def out_id(self, value):
        self._out_id = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def publish_time(self):
        return self._publish_time

    @publish_time.setter
    def publish_time(self, value):
        self._publish_time = value
    @property
    def publisher(self):
        return self._publisher

    @publisher.setter
    def publisher(self, value):
        self._publisher = value
    @property
    def service_type(self):
        return self._service_type

    @service_type.setter
    def service_type(self, value):
        self._service_type = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def street(self):
        return self._street

    @street.setter
    def street(self, value):
        self._street = value
    @property
    def sub_biz_type(self):
        return self._sub_biz_type

    @sub_biz_type.setter
    def sub_biz_type(self, value):
        self._sub_biz_type = value
    @property
    def template_content(self):
        return self._template_content

    @template_content.setter
    def template_content(self, value):
        self._template_content = value
    @property
    def template_type(self):
        return self._template_type

    @template_type.setter
    def template_type(self, value):
        self._template_type = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.community:
            if hasattr(self.community, 'to_alipay_dict'):
                params['community'] = self.community.to_alipay_dict()
            else:
                params['community'] = self.community
        if self.community_short_name:
            if hasattr(self.community_short_name, 'to_alipay_dict'):
                params['community_short_name'] = self.community_short_name.to_alipay_dict()
            else:
                params['community_short_name'] = self.community_short_name
        if self.county:
            if hasattr(self.county, 'to_alipay_dict'):
                params['county'] = self.county.to_alipay_dict()
            else:
                params['county'] = self.county
        if self.expired_time:
            if hasattr(self.expired_time, 'to_alipay_dict'):
                params['expired_time'] = self.expired_time.to_alipay_dict()
            else:
                params['expired_time'] = self.expired_time
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.is_top:
            if hasattr(self.is_top, 'to_alipay_dict'):
                params['is_top'] = self.is_top.to_alipay_dict()
            else:
                params['is_top'] = self.is_top
        if self.link_url:
            if hasattr(self.link_url, 'to_alipay_dict'):
                params['link_url'] = self.link_url.to_alipay_dict()
            else:
                params['link_url'] = self.link_url
        if self.out_id:
            if hasattr(self.out_id, 'to_alipay_dict'):
                params['out_id'] = self.out_id.to_alipay_dict()
            else:
                params['out_id'] = self.out_id
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        if self.publish_time:
            if hasattr(self.publish_time, 'to_alipay_dict'):
                params['publish_time'] = self.publish_time.to_alipay_dict()
            else:
                params['publish_time'] = self.publish_time
        if self.publisher:
            if hasattr(self.publisher, 'to_alipay_dict'):
                params['publisher'] = self.publisher.to_alipay_dict()
            else:
                params['publisher'] = self.publisher
        if self.service_type:
            if hasattr(self.service_type, 'to_alipay_dict'):
                params['service_type'] = self.service_type.to_alipay_dict()
            else:
                params['service_type'] = self.service_type
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.street:
            if hasattr(self.street, 'to_alipay_dict'):
                params['street'] = self.street.to_alipay_dict()
            else:
                params['street'] = self.street
        if self.sub_biz_type:
            if hasattr(self.sub_biz_type, 'to_alipay_dict'):
                params['sub_biz_type'] = self.sub_biz_type.to_alipay_dict()
            else:
                params['sub_biz_type'] = self.sub_biz_type
        if self.template_content:
            if hasattr(self.template_content, 'to_alipay_dict'):
                params['template_content'] = self.template_content.to_alipay_dict()
            else:
                params['template_content'] = self.template_content
        if self.template_type:
            if hasattr(self.template_type, 'to_alipay_dict'):
                params['template_type'] = self.template_type.to_alipay_dict()
            else:
                params['template_type'] = self.template_type
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppCommunityOwnercardmsgSyncModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'city' in d:
            o.city = d['city']
        if 'community' in d:
            o.community = d['community']
        if 'community_short_name' in d:
            o.community_short_name = d['community_short_name']
        if 'county' in d:
            o.county = d['county']
        if 'expired_time' in d:
            o.expired_time = d['expired_time']
        if 'id' in d:
            o.id = d['id']
        if 'is_top' in d:
            o.is_top = d['is_top']
        if 'link_url' in d:
            o.link_url = d['link_url']
        if 'out_id' in d:
            o.out_id = d['out_id']
        if 'province' in d:
            o.province = d['province']
        if 'publish_time' in d:
            o.publish_time = d['publish_time']
        if 'publisher' in d:
            o.publisher = d['publisher']
        if 'service_type' in d:
            o.service_type = d['service_type']
        if 'status' in d:
            o.status = d['status']
        if 'street' in d:
            o.street = d['street']
        if 'sub_biz_type' in d:
            o.sub_biz_type = d['sub_biz_type']
        if 'template_content' in d:
            o.template_content = d['template_content']
        if 'template_type' in d:
            o.template_type = d['template_type']
        if 'title' in d:
            o.title = d['title']
        return o


