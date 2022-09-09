#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GiftTemplateBaseInfo(object):

    def __init__(self):
        self._card_image_url = None
        self._link_show_memo = None
        self._link_to_get = None
        self._memo = None
        self._name = None
        self._share_desc = None
        self._share_title = None
        self._share_url = None
        self._template_form_thumbnail_url = None
        self._template_thumbnail = None

    @property
    def card_image_url(self):
        return self._card_image_url

    @card_image_url.setter
    def card_image_url(self, value):
        self._card_image_url = value
    @property
    def link_show_memo(self):
        return self._link_show_memo

    @link_show_memo.setter
    def link_show_memo(self, value):
        self._link_show_memo = value
    @property
    def link_to_get(self):
        return self._link_to_get

    @link_to_get.setter
    def link_to_get(self, value):
        self._link_to_get = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def share_desc(self):
        return self._share_desc

    @share_desc.setter
    def share_desc(self, value):
        self._share_desc = value
    @property
    def share_title(self):
        return self._share_title

    @share_title.setter
    def share_title(self, value):
        self._share_title = value
    @property
    def share_url(self):
        return self._share_url

    @share_url.setter
    def share_url(self, value):
        self._share_url = value
    @property
    def template_form_thumbnail_url(self):
        return self._template_form_thumbnail_url

    @template_form_thumbnail_url.setter
    def template_form_thumbnail_url(self, value):
        self._template_form_thumbnail_url = value
    @property
    def template_thumbnail(self):
        return self._template_thumbnail

    @template_thumbnail.setter
    def template_thumbnail(self, value):
        self._template_thumbnail = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_image_url:
            if hasattr(self.card_image_url, 'to_alipay_dict'):
                params['card_image_url'] = self.card_image_url.to_alipay_dict()
            else:
                params['card_image_url'] = self.card_image_url
        if self.link_show_memo:
            if hasattr(self.link_show_memo, 'to_alipay_dict'):
                params['link_show_memo'] = self.link_show_memo.to_alipay_dict()
            else:
                params['link_show_memo'] = self.link_show_memo
        if self.link_to_get:
            if hasattr(self.link_to_get, 'to_alipay_dict'):
                params['link_to_get'] = self.link_to_get.to_alipay_dict()
            else:
                params['link_to_get'] = self.link_to_get
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.share_desc:
            if hasattr(self.share_desc, 'to_alipay_dict'):
                params['share_desc'] = self.share_desc.to_alipay_dict()
            else:
                params['share_desc'] = self.share_desc
        if self.share_title:
            if hasattr(self.share_title, 'to_alipay_dict'):
                params['share_title'] = self.share_title.to_alipay_dict()
            else:
                params['share_title'] = self.share_title
        if self.share_url:
            if hasattr(self.share_url, 'to_alipay_dict'):
                params['share_url'] = self.share_url.to_alipay_dict()
            else:
                params['share_url'] = self.share_url
        if self.template_form_thumbnail_url:
            if hasattr(self.template_form_thumbnail_url, 'to_alipay_dict'):
                params['template_form_thumbnail_url'] = self.template_form_thumbnail_url.to_alipay_dict()
            else:
                params['template_form_thumbnail_url'] = self.template_form_thumbnail_url
        if self.template_thumbnail:
            if hasattr(self.template_thumbnail, 'to_alipay_dict'):
                params['template_thumbnail'] = self.template_thumbnail.to_alipay_dict()
            else:
                params['template_thumbnail'] = self.template_thumbnail
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GiftTemplateBaseInfo()
        if 'card_image_url' in d:
            o.card_image_url = d['card_image_url']
        if 'link_show_memo' in d:
            o.link_show_memo = d['link_show_memo']
        if 'link_to_get' in d:
            o.link_to_get = d['link_to_get']
        if 'memo' in d:
            o.memo = d['memo']
        if 'name' in d:
            o.name = d['name']
        if 'share_desc' in d:
            o.share_desc = d['share_desc']
        if 'share_title' in d:
            o.share_title = d['share_title']
        if 'share_url' in d:
            o.share_url = d['share_url']
        if 'template_form_thumbnail_url' in d:
            o.template_form_thumbnail_url = d['template_form_thumbnail_url']
        if 'template_thumbnail' in d:
            o.template_thumbnail = d['template_thumbnail']
        return o


