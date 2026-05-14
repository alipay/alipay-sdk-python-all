#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MiniAppServiceBatchQueryResult(object):

    def __init__(self):
        self._aggre_sales = None
        self._available = None
        self._detail_url = None
        self._expert_remark = None
        self._expert_remark_icon = None
        self._featured_labels = None
        self._item_id = None
        self._marketing_labels = None
        self._point = None
        self._point_preferential_yuan = None
        self._rank_link = None
        self._rank_pos = None
        self._reason_desc = None
        self._service_id = None
        self._sub_cat_name = None
        self._yuan = None

    @property
    def aggre_sales(self):
        return self._aggre_sales

    @aggre_sales.setter
    def aggre_sales(self, value):
        self._aggre_sales = value
    @property
    def available(self):
        return self._available

    @available.setter
    def available(self, value):
        self._available = value
    @property
    def detail_url(self):
        return self._detail_url

    @detail_url.setter
    def detail_url(self, value):
        self._detail_url = value
    @property
    def expert_remark(self):
        return self._expert_remark

    @expert_remark.setter
    def expert_remark(self, value):
        self._expert_remark = value
    @property
    def expert_remark_icon(self):
        return self._expert_remark_icon

    @expert_remark_icon.setter
    def expert_remark_icon(self, value):
        self._expert_remark_icon = value
    @property
    def featured_labels(self):
        return self._featured_labels

    @featured_labels.setter
    def featured_labels(self, value):
        if isinstance(value, list):
            self._featured_labels = list()
            for i in value:
                self._featured_labels.append(i)
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def marketing_labels(self):
        return self._marketing_labels

    @marketing_labels.setter
    def marketing_labels(self, value):
        if isinstance(value, list):
            self._marketing_labels = list()
            for i in value:
                self._marketing_labels.append(i)
    @property
    def point(self):
        return self._point

    @point.setter
    def point(self, value):
        self._point = value
    @property
    def point_preferential_yuan(self):
        return self._point_preferential_yuan

    @point_preferential_yuan.setter
    def point_preferential_yuan(self, value):
        self._point_preferential_yuan = value
    @property
    def rank_link(self):
        return self._rank_link

    @rank_link.setter
    def rank_link(self, value):
        self._rank_link = value
    @property
    def rank_pos(self):
        return self._rank_pos

    @rank_pos.setter
    def rank_pos(self, value):
        self._rank_pos = value
    @property
    def reason_desc(self):
        return self._reason_desc

    @reason_desc.setter
    def reason_desc(self, value):
        self._reason_desc = value
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value
    @property
    def sub_cat_name(self):
        return self._sub_cat_name

    @sub_cat_name.setter
    def sub_cat_name(self, value):
        self._sub_cat_name = value
    @property
    def yuan(self):
        return self._yuan

    @yuan.setter
    def yuan(self, value):
        self._yuan = value


    def to_alipay_dict(self):
        params = dict()
        if self.aggre_sales:
            if hasattr(self.aggre_sales, 'to_alipay_dict'):
                params['aggre_sales'] = self.aggre_sales.to_alipay_dict()
            else:
                params['aggre_sales'] = self.aggre_sales
        if self.available:
            if hasattr(self.available, 'to_alipay_dict'):
                params['available'] = self.available.to_alipay_dict()
            else:
                params['available'] = self.available
        if self.detail_url:
            if hasattr(self.detail_url, 'to_alipay_dict'):
                params['detail_url'] = self.detail_url.to_alipay_dict()
            else:
                params['detail_url'] = self.detail_url
        if self.expert_remark:
            if hasattr(self.expert_remark, 'to_alipay_dict'):
                params['expert_remark'] = self.expert_remark.to_alipay_dict()
            else:
                params['expert_remark'] = self.expert_remark
        if self.expert_remark_icon:
            if hasattr(self.expert_remark_icon, 'to_alipay_dict'):
                params['expert_remark_icon'] = self.expert_remark_icon.to_alipay_dict()
            else:
                params['expert_remark_icon'] = self.expert_remark_icon
        if self.featured_labels:
            if isinstance(self.featured_labels, list):
                for i in range(0, len(self.featured_labels)):
                    element = self.featured_labels[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.featured_labels[i] = element.to_alipay_dict()
            if hasattr(self.featured_labels, 'to_alipay_dict'):
                params['featured_labels'] = self.featured_labels.to_alipay_dict()
            else:
                params['featured_labels'] = self.featured_labels
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.marketing_labels:
            if isinstance(self.marketing_labels, list):
                for i in range(0, len(self.marketing_labels)):
                    element = self.marketing_labels[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.marketing_labels[i] = element.to_alipay_dict()
            if hasattr(self.marketing_labels, 'to_alipay_dict'):
                params['marketing_labels'] = self.marketing_labels.to_alipay_dict()
            else:
                params['marketing_labels'] = self.marketing_labels
        if self.point:
            if hasattr(self.point, 'to_alipay_dict'):
                params['point'] = self.point.to_alipay_dict()
            else:
                params['point'] = self.point
        if self.point_preferential_yuan:
            if hasattr(self.point_preferential_yuan, 'to_alipay_dict'):
                params['point_preferential_yuan'] = self.point_preferential_yuan.to_alipay_dict()
            else:
                params['point_preferential_yuan'] = self.point_preferential_yuan
        if self.rank_link:
            if hasattr(self.rank_link, 'to_alipay_dict'):
                params['rank_link'] = self.rank_link.to_alipay_dict()
            else:
                params['rank_link'] = self.rank_link
        if self.rank_pos:
            if hasattr(self.rank_pos, 'to_alipay_dict'):
                params['rank_pos'] = self.rank_pos.to_alipay_dict()
            else:
                params['rank_pos'] = self.rank_pos
        if self.reason_desc:
            if hasattr(self.reason_desc, 'to_alipay_dict'):
                params['reason_desc'] = self.reason_desc.to_alipay_dict()
            else:
                params['reason_desc'] = self.reason_desc
        if self.service_id:
            if hasattr(self.service_id, 'to_alipay_dict'):
                params['service_id'] = self.service_id.to_alipay_dict()
            else:
                params['service_id'] = self.service_id
        if self.sub_cat_name:
            if hasattr(self.sub_cat_name, 'to_alipay_dict'):
                params['sub_cat_name'] = self.sub_cat_name.to_alipay_dict()
            else:
                params['sub_cat_name'] = self.sub_cat_name
        if self.yuan:
            if hasattr(self.yuan, 'to_alipay_dict'):
                params['yuan'] = self.yuan.to_alipay_dict()
            else:
                params['yuan'] = self.yuan
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MiniAppServiceBatchQueryResult()
        if 'aggre_sales' in d:
            o.aggre_sales = d['aggre_sales']
        if 'available' in d:
            o.available = d['available']
        if 'detail_url' in d:
            o.detail_url = d['detail_url']
        if 'expert_remark' in d:
            o.expert_remark = d['expert_remark']
        if 'expert_remark_icon' in d:
            o.expert_remark_icon = d['expert_remark_icon']
        if 'featured_labels' in d:
            o.featured_labels = d['featured_labels']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'marketing_labels' in d:
            o.marketing_labels = d['marketing_labels']
        if 'point' in d:
            o.point = d['point']
        if 'point_preferential_yuan' in d:
            o.point_preferential_yuan = d['point_preferential_yuan']
        if 'rank_link' in d:
            o.rank_link = d['rank_link']
        if 'rank_pos' in d:
            o.rank_pos = d['rank_pos']
        if 'reason_desc' in d:
            o.reason_desc = d['reason_desc']
        if 'service_id' in d:
            o.service_id = d['service_id']
        if 'sub_cat_name' in d:
            o.sub_cat_name = d['sub_cat_name']
        if 'yuan' in d:
            o.yuan = d['yuan']
        return o


