#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppCommunityNoticePublishModel(object):

    def __init__(self):
        self._biz_type = None
        self._city = None
        self._community = None
        self._county = None
        self._detail_link_url = None
        self._expired_time = None
        self._is_top = None
        self._list_link_url = None
        self._notice_type = None
        self._out_community_id = None
        self._out_notice_id = None
        self._province = None
        self._publisher = None
        self._street = None
        self._sub_biz_type = None
        self._sub_notice_type = None
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
    def county(self):
        return self._county

    @county.setter
    def county(self, value):
        self._county = value
    @property
    def detail_link_url(self):
        return self._detail_link_url

    @detail_link_url.setter
    def detail_link_url(self, value):
        self._detail_link_url = value
    @property
    def expired_time(self):
        return self._expired_time

    @expired_time.setter
    def expired_time(self, value):
        self._expired_time = value
    @property
    def is_top(self):
        return self._is_top

    @is_top.setter
    def is_top(self, value):
        self._is_top = value
    @property
    def list_link_url(self):
        return self._list_link_url

    @list_link_url.setter
    def list_link_url(self, value):
        self._list_link_url = value
    @property
    def notice_type(self):
        return self._notice_type

    @notice_type.setter
    def notice_type(self, value):
        self._notice_type = value
    @property
    def out_community_id(self):
        return self._out_community_id

    @out_community_id.setter
    def out_community_id(self, value):
        self._out_community_id = value
    @property
    def out_notice_id(self):
        return self._out_notice_id

    @out_notice_id.setter
    def out_notice_id(self, value):
        self._out_notice_id = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def publisher(self):
        return self._publisher

    @publisher.setter
    def publisher(self, value):
        self._publisher = value
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
    def sub_notice_type(self):
        return self._sub_notice_type

    @sub_notice_type.setter
    def sub_notice_type(self, value):
        self._sub_notice_type = value
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
        if self.county:
            if hasattr(self.county, 'to_alipay_dict'):
                params['county'] = self.county.to_alipay_dict()
            else:
                params['county'] = self.county
        if self.detail_link_url:
            if hasattr(self.detail_link_url, 'to_alipay_dict'):
                params['detail_link_url'] = self.detail_link_url.to_alipay_dict()
            else:
                params['detail_link_url'] = self.detail_link_url
        if self.expired_time:
            if hasattr(self.expired_time, 'to_alipay_dict'):
                params['expired_time'] = self.expired_time.to_alipay_dict()
            else:
                params['expired_time'] = self.expired_time
        if self.is_top:
            if hasattr(self.is_top, 'to_alipay_dict'):
                params['is_top'] = self.is_top.to_alipay_dict()
            else:
                params['is_top'] = self.is_top
        if self.list_link_url:
            if hasattr(self.list_link_url, 'to_alipay_dict'):
                params['list_link_url'] = self.list_link_url.to_alipay_dict()
            else:
                params['list_link_url'] = self.list_link_url
        if self.notice_type:
            if hasattr(self.notice_type, 'to_alipay_dict'):
                params['notice_type'] = self.notice_type.to_alipay_dict()
            else:
                params['notice_type'] = self.notice_type
        if self.out_community_id:
            if hasattr(self.out_community_id, 'to_alipay_dict'):
                params['out_community_id'] = self.out_community_id.to_alipay_dict()
            else:
                params['out_community_id'] = self.out_community_id
        if self.out_notice_id:
            if hasattr(self.out_notice_id, 'to_alipay_dict'):
                params['out_notice_id'] = self.out_notice_id.to_alipay_dict()
            else:
                params['out_notice_id'] = self.out_notice_id
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        if self.publisher:
            if hasattr(self.publisher, 'to_alipay_dict'):
                params['publisher'] = self.publisher.to_alipay_dict()
            else:
                params['publisher'] = self.publisher
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
        if self.sub_notice_type:
            if hasattr(self.sub_notice_type, 'to_alipay_dict'):
                params['sub_notice_type'] = self.sub_notice_type.to_alipay_dict()
            else:
                params['sub_notice_type'] = self.sub_notice_type
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
        o = AlipayEbppCommunityNoticePublishModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'city' in d:
            o.city = d['city']
        if 'community' in d:
            o.community = d['community']
        if 'county' in d:
            o.county = d['county']
        if 'detail_link_url' in d:
            o.detail_link_url = d['detail_link_url']
        if 'expired_time' in d:
            o.expired_time = d['expired_time']
        if 'is_top' in d:
            o.is_top = d['is_top']
        if 'list_link_url' in d:
            o.list_link_url = d['list_link_url']
        if 'notice_type' in d:
            o.notice_type = d['notice_type']
        if 'out_community_id' in d:
            o.out_community_id = d['out_community_id']
        if 'out_notice_id' in d:
            o.out_notice_id = d['out_notice_id']
        if 'province' in d:
            o.province = d['province']
        if 'publisher' in d:
            o.publisher = d['publisher']
        if 'street' in d:
            o.street = d['street']
        if 'sub_biz_type' in d:
            o.sub_biz_type = d['sub_biz_type']
        if 'sub_notice_type' in d:
            o.sub_notice_type = d['sub_notice_type']
        if 'title' in d:
            o.title = d['title']
        return o


