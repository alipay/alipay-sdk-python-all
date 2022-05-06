#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ImageTemplateData import ImageTemplateData
from alipay.aop.api.domain.LinksTemplateData import LinksTemplateData
from alipay.aop.api.domain.MiniAppTemplateData import MiniAppTemplateData
from alipay.aop.api.domain.TextTemplateData import TextTemplateData


class AlipaySocialBaseBcClustermsgSendModel(object):

    def __init__(self):
        self._at_all = None
        self._biz_id = None
        self._cluster_ids = None
        self._image_template_data = None
        self._links_template_data = None
        self._miniapp_template_data = None
        self._msg_name = None
        self._operate_business_id = None
        self._template_code = None
        self._tenant_id = None
        self._text_template_data = None

    @property
    def at_all(self):
        return self._at_all

    @at_all.setter
    def at_all(self, value):
        self._at_all = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def cluster_ids(self):
        return self._cluster_ids

    @cluster_ids.setter
    def cluster_ids(self, value):
        if isinstance(value, list):
            self._cluster_ids = list()
            for i in value:
                self._cluster_ids.append(i)
    @property
    def image_template_data(self):
        return self._image_template_data

    @image_template_data.setter
    def image_template_data(self, value):
        if isinstance(value, ImageTemplateData):
            self._image_template_data = value
        else:
            self._image_template_data = ImageTemplateData.from_alipay_dict(value)
    @property
    def links_template_data(self):
        return self._links_template_data

    @links_template_data.setter
    def links_template_data(self, value):
        if isinstance(value, LinksTemplateData):
            self._links_template_data = value
        else:
            self._links_template_data = LinksTemplateData.from_alipay_dict(value)
    @property
    def miniapp_template_data(self):
        return self._miniapp_template_data

    @miniapp_template_data.setter
    def miniapp_template_data(self, value):
        if isinstance(value, MiniAppTemplateData):
            self._miniapp_template_data = value
        else:
            self._miniapp_template_data = MiniAppTemplateData.from_alipay_dict(value)
    @property
    def msg_name(self):
        return self._msg_name

    @msg_name.setter
    def msg_name(self, value):
        self._msg_name = value
    @property
    def operate_business_id(self):
        return self._operate_business_id

    @operate_business_id.setter
    def operate_business_id(self, value):
        self._operate_business_id = value
    @property
    def template_code(self):
        return self._template_code

    @template_code.setter
    def template_code(self, value):
        self._template_code = value
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value
    @property
    def text_template_data(self):
        return self._text_template_data

    @text_template_data.setter
    def text_template_data(self, value):
        if isinstance(value, TextTemplateData):
            self._text_template_data = value
        else:
            self._text_template_data = TextTemplateData.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.at_all:
            if hasattr(self.at_all, 'to_alipay_dict'):
                params['at_all'] = self.at_all.to_alipay_dict()
            else:
                params['at_all'] = self.at_all
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.cluster_ids:
            if isinstance(self.cluster_ids, list):
                for i in range(0, len(self.cluster_ids)):
                    element = self.cluster_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.cluster_ids[i] = element.to_alipay_dict()
            if hasattr(self.cluster_ids, 'to_alipay_dict'):
                params['cluster_ids'] = self.cluster_ids.to_alipay_dict()
            else:
                params['cluster_ids'] = self.cluster_ids
        if self.image_template_data:
            if hasattr(self.image_template_data, 'to_alipay_dict'):
                params['image_template_data'] = self.image_template_data.to_alipay_dict()
            else:
                params['image_template_data'] = self.image_template_data
        if self.links_template_data:
            if hasattr(self.links_template_data, 'to_alipay_dict'):
                params['links_template_data'] = self.links_template_data.to_alipay_dict()
            else:
                params['links_template_data'] = self.links_template_data
        if self.miniapp_template_data:
            if hasattr(self.miniapp_template_data, 'to_alipay_dict'):
                params['miniapp_template_data'] = self.miniapp_template_data.to_alipay_dict()
            else:
                params['miniapp_template_data'] = self.miniapp_template_data
        if self.msg_name:
            if hasattr(self.msg_name, 'to_alipay_dict'):
                params['msg_name'] = self.msg_name.to_alipay_dict()
            else:
                params['msg_name'] = self.msg_name
        if self.operate_business_id:
            if hasattr(self.operate_business_id, 'to_alipay_dict'):
                params['operate_business_id'] = self.operate_business_id.to_alipay_dict()
            else:
                params['operate_business_id'] = self.operate_business_id
        if self.template_code:
            if hasattr(self.template_code, 'to_alipay_dict'):
                params['template_code'] = self.template_code.to_alipay_dict()
            else:
                params['template_code'] = self.template_code
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
        if self.text_template_data:
            if hasattr(self.text_template_data, 'to_alipay_dict'):
                params['text_template_data'] = self.text_template_data.to_alipay_dict()
            else:
                params['text_template_data'] = self.text_template_data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySocialBaseBcClustermsgSendModel()
        if 'at_all' in d:
            o.at_all = d['at_all']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'cluster_ids' in d:
            o.cluster_ids = d['cluster_ids']
        if 'image_template_data' in d:
            o.image_template_data = d['image_template_data']
        if 'links_template_data' in d:
            o.links_template_data = d['links_template_data']
        if 'miniapp_template_data' in d:
            o.miniapp_template_data = d['miniapp_template_data']
        if 'msg_name' in d:
            o.msg_name = d['msg_name']
        if 'operate_business_id' in d:
            o.operate_business_id = d['operate_business_id']
        if 'template_code' in d:
            o.template_code = d['template_code']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        if 'text_template_data' in d:
            o.text_template_data = d['text_template_data']
        return o


