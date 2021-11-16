#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OrderStatusData import OrderStatusData
from alipay.aop.api.domain.OrderStatusData import OrderStatusData
from alipay.aop.api.domain.OrderStatusData import OrderStatusData
from alipay.aop.api.domain.SearchOrderDetailDataBaseItems import SearchOrderDetailDataBaseItems
from alipay.aop.api.domain.SearchOrderDetailDataBrandItems import SearchOrderDetailDataBrandItems
from alipay.aop.api.domain.SearchOrderDetailDataServiceItems import SearchOrderDetailDataServiceItems


class SearchOrderDetailData(object):

    def __init__(self):
        self._access_type = None
        self._app_category = None
        self._app_icon = None
        self._app_name = None
        self._app_status = None
        self._appid = None
        self._base_order_status = None
        self._biz_id = None
        self._box_order_status = None
        self._box_status = None
        self._brand_template_id = None
        self._brandbox_orderstatus = None
        self._can_modify_keyword = None
        self._describe = None
        self._detail_base_items = None
        self._detail_brand_items = None
        self._detail_service_items = None
        self._final_status = None
        self._gmtmodified = None
        self._keyword_gmt_modified = None
        self._online_time = None
        self._operator_type = None
        self._order_id = None
        self._partner_type = None
        self._reject_node = None
        self._reject_reason = None
        self._scene_code = None
        self._scene_name = None
        self._service_code = None
        self._service_name = None
        self._status = None
        self._sub_service_code = None
        self._template_id = None
        self._template_name = None

    @property
    def access_type(self):
        return self._access_type

    @access_type.setter
    def access_type(self, value):
        self._access_type = value
    @property
    def app_category(self):
        return self._app_category

    @app_category.setter
    def app_category(self, value):
        self._app_category = value
    @property
    def app_icon(self):
        return self._app_icon

    @app_icon.setter
    def app_icon(self, value):
        self._app_icon = value
    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def app_status(self):
        return self._app_status

    @app_status.setter
    def app_status(self, value):
        self._app_status = value
    @property
    def appid(self):
        return self._appid

    @appid.setter
    def appid(self, value):
        self._appid = value
    @property
    def base_order_status(self):
        return self._base_order_status

    @base_order_status.setter
    def base_order_status(self, value):
        if isinstance(value, OrderStatusData):
            self._base_order_status = value
        else:
            self._base_order_status = OrderStatusData.from_alipay_dict(value)
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def box_order_status(self):
        return self._box_order_status

    @box_order_status.setter
    def box_order_status(self, value):
        if isinstance(value, OrderStatusData):
            self._box_order_status = value
        else:
            self._box_order_status = OrderStatusData.from_alipay_dict(value)
    @property
    def box_status(self):
        return self._box_status

    @box_status.setter
    def box_status(self, value):
        self._box_status = value
    @property
    def brand_template_id(self):
        return self._brand_template_id

    @brand_template_id.setter
    def brand_template_id(self, value):
        self._brand_template_id = value
    @property
    def brandbox_orderstatus(self):
        return self._brandbox_orderstatus

    @brandbox_orderstatus.setter
    def brandbox_orderstatus(self, value):
        if isinstance(value, OrderStatusData):
            self._brandbox_orderstatus = value
        else:
            self._brandbox_orderstatus = OrderStatusData.from_alipay_dict(value)
    @property
    def can_modify_keyword(self):
        return self._can_modify_keyword

    @can_modify_keyword.setter
    def can_modify_keyword(self, value):
        self._can_modify_keyword = value
    @property
    def describe(self):
        return self._describe

    @describe.setter
    def describe(self, value):
        self._describe = value
    @property
    def detail_base_items(self):
        return self._detail_base_items

    @detail_base_items.setter
    def detail_base_items(self, value):
        if isinstance(value, SearchOrderDetailDataBaseItems):
            self._detail_base_items = value
        else:
            self._detail_base_items = SearchOrderDetailDataBaseItems.from_alipay_dict(value)
    @property
    def detail_brand_items(self):
        return self._detail_brand_items

    @detail_brand_items.setter
    def detail_brand_items(self, value):
        if isinstance(value, SearchOrderDetailDataBrandItems):
            self._detail_brand_items = value
        else:
            self._detail_brand_items = SearchOrderDetailDataBrandItems.from_alipay_dict(value)
    @property
    def detail_service_items(self):
        return self._detail_service_items

    @detail_service_items.setter
    def detail_service_items(self, value):
        if isinstance(value, SearchOrderDetailDataServiceItems):
            self._detail_service_items = value
        else:
            self._detail_service_items = SearchOrderDetailDataServiceItems.from_alipay_dict(value)
    @property
    def final_status(self):
        return self._final_status

    @final_status.setter
    def final_status(self, value):
        self._final_status = value
    @property
    def gmtmodified(self):
        return self._gmtmodified

    @gmtmodified.setter
    def gmtmodified(self, value):
        self._gmtmodified = value
    @property
    def keyword_gmt_modified(self):
        return self._keyword_gmt_modified

    @keyword_gmt_modified.setter
    def keyword_gmt_modified(self, value):
        self._keyword_gmt_modified = value
    @property
    def online_time(self):
        return self._online_time

    @online_time.setter
    def online_time(self, value):
        self._online_time = value
    @property
    def operator_type(self):
        return self._operator_type

    @operator_type.setter
    def operator_type(self, value):
        self._operator_type = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def partner_type(self):
        return self._partner_type

    @partner_type.setter
    def partner_type(self, value):
        self._partner_type = value
    @property
    def reject_node(self):
        return self._reject_node

    @reject_node.setter
    def reject_node(self, value):
        self._reject_node = value
    @property
    def reject_reason(self):
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, value):
        self._reject_reason = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def scene_name(self):
        return self._scene_name

    @scene_name.setter
    def scene_name(self, value):
        self._scene_name = value
    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value
    @property
    def service_name(self):
        return self._service_name

    @service_name.setter
    def service_name(self, value):
        self._service_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sub_service_code(self):
        return self._sub_service_code

    @sub_service_code.setter
    def sub_service_code(self, value):
        self._sub_service_code = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def template_name(self):
        return self._template_name

    @template_name.setter
    def template_name(self, value):
        self._template_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.access_type:
            if hasattr(self.access_type, 'to_alipay_dict'):
                params['access_type'] = self.access_type.to_alipay_dict()
            else:
                params['access_type'] = self.access_type
        if self.app_category:
            if hasattr(self.app_category, 'to_alipay_dict'):
                params['app_category'] = self.app_category.to_alipay_dict()
            else:
                params['app_category'] = self.app_category
        if self.app_icon:
            if hasattr(self.app_icon, 'to_alipay_dict'):
                params['app_icon'] = self.app_icon.to_alipay_dict()
            else:
                params['app_icon'] = self.app_icon
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.app_status:
            if hasattr(self.app_status, 'to_alipay_dict'):
                params['app_status'] = self.app_status.to_alipay_dict()
            else:
                params['app_status'] = self.app_status
        if self.appid:
            if hasattr(self.appid, 'to_alipay_dict'):
                params['appid'] = self.appid.to_alipay_dict()
            else:
                params['appid'] = self.appid
        if self.base_order_status:
            if hasattr(self.base_order_status, 'to_alipay_dict'):
                params['base_order_status'] = self.base_order_status.to_alipay_dict()
            else:
                params['base_order_status'] = self.base_order_status
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.box_order_status:
            if hasattr(self.box_order_status, 'to_alipay_dict'):
                params['box_order_status'] = self.box_order_status.to_alipay_dict()
            else:
                params['box_order_status'] = self.box_order_status
        if self.box_status:
            if hasattr(self.box_status, 'to_alipay_dict'):
                params['box_status'] = self.box_status.to_alipay_dict()
            else:
                params['box_status'] = self.box_status
        if self.brand_template_id:
            if hasattr(self.brand_template_id, 'to_alipay_dict'):
                params['brand_template_id'] = self.brand_template_id.to_alipay_dict()
            else:
                params['brand_template_id'] = self.brand_template_id
        if self.brandbox_orderstatus:
            if hasattr(self.brandbox_orderstatus, 'to_alipay_dict'):
                params['brandbox_orderstatus'] = self.brandbox_orderstatus.to_alipay_dict()
            else:
                params['brandbox_orderstatus'] = self.brandbox_orderstatus
        if self.can_modify_keyword:
            if hasattr(self.can_modify_keyword, 'to_alipay_dict'):
                params['can_modify_keyword'] = self.can_modify_keyword.to_alipay_dict()
            else:
                params['can_modify_keyword'] = self.can_modify_keyword
        if self.describe:
            if hasattr(self.describe, 'to_alipay_dict'):
                params['describe'] = self.describe.to_alipay_dict()
            else:
                params['describe'] = self.describe
        if self.detail_base_items:
            if hasattr(self.detail_base_items, 'to_alipay_dict'):
                params['detail_base_items'] = self.detail_base_items.to_alipay_dict()
            else:
                params['detail_base_items'] = self.detail_base_items
        if self.detail_brand_items:
            if hasattr(self.detail_brand_items, 'to_alipay_dict'):
                params['detail_brand_items'] = self.detail_brand_items.to_alipay_dict()
            else:
                params['detail_brand_items'] = self.detail_brand_items
        if self.detail_service_items:
            if hasattr(self.detail_service_items, 'to_alipay_dict'):
                params['detail_service_items'] = self.detail_service_items.to_alipay_dict()
            else:
                params['detail_service_items'] = self.detail_service_items
        if self.final_status:
            if hasattr(self.final_status, 'to_alipay_dict'):
                params['final_status'] = self.final_status.to_alipay_dict()
            else:
                params['final_status'] = self.final_status
        if self.gmtmodified:
            if hasattr(self.gmtmodified, 'to_alipay_dict'):
                params['gmtmodified'] = self.gmtmodified.to_alipay_dict()
            else:
                params['gmtmodified'] = self.gmtmodified
        if self.keyword_gmt_modified:
            if hasattr(self.keyword_gmt_modified, 'to_alipay_dict'):
                params['keyword_gmt_modified'] = self.keyword_gmt_modified.to_alipay_dict()
            else:
                params['keyword_gmt_modified'] = self.keyword_gmt_modified
        if self.online_time:
            if hasattr(self.online_time, 'to_alipay_dict'):
                params['online_time'] = self.online_time.to_alipay_dict()
            else:
                params['online_time'] = self.online_time
        if self.operator_type:
            if hasattr(self.operator_type, 'to_alipay_dict'):
                params['operator_type'] = self.operator_type.to_alipay_dict()
            else:
                params['operator_type'] = self.operator_type
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.partner_type:
            if hasattr(self.partner_type, 'to_alipay_dict'):
                params['partner_type'] = self.partner_type.to_alipay_dict()
            else:
                params['partner_type'] = self.partner_type
        if self.reject_node:
            if hasattr(self.reject_node, 'to_alipay_dict'):
                params['reject_node'] = self.reject_node.to_alipay_dict()
            else:
                params['reject_node'] = self.reject_node
        if self.reject_reason:
            if hasattr(self.reject_reason, 'to_alipay_dict'):
                params['reject_reason'] = self.reject_reason.to_alipay_dict()
            else:
                params['reject_reason'] = self.reject_reason
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.scene_name:
            if hasattr(self.scene_name, 'to_alipay_dict'):
                params['scene_name'] = self.scene_name.to_alipay_dict()
            else:
                params['scene_name'] = self.scene_name
        if self.service_code:
            if hasattr(self.service_code, 'to_alipay_dict'):
                params['service_code'] = self.service_code.to_alipay_dict()
            else:
                params['service_code'] = self.service_code
        if self.service_name:
            if hasattr(self.service_name, 'to_alipay_dict'):
                params['service_name'] = self.service_name.to_alipay_dict()
            else:
                params['service_name'] = self.service_name
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.sub_service_code:
            if hasattr(self.sub_service_code, 'to_alipay_dict'):
                params['sub_service_code'] = self.sub_service_code.to_alipay_dict()
            else:
                params['sub_service_code'] = self.sub_service_code
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.template_name:
            if hasattr(self.template_name, 'to_alipay_dict'):
                params['template_name'] = self.template_name.to_alipay_dict()
            else:
                params['template_name'] = self.template_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SearchOrderDetailData()
        if 'access_type' in d:
            o.access_type = d['access_type']
        if 'app_category' in d:
            o.app_category = d['app_category']
        if 'app_icon' in d:
            o.app_icon = d['app_icon']
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'app_status' in d:
            o.app_status = d['app_status']
        if 'appid' in d:
            o.appid = d['appid']
        if 'base_order_status' in d:
            o.base_order_status = d['base_order_status']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'box_order_status' in d:
            o.box_order_status = d['box_order_status']
        if 'box_status' in d:
            o.box_status = d['box_status']
        if 'brand_template_id' in d:
            o.brand_template_id = d['brand_template_id']
        if 'brandbox_orderstatus' in d:
            o.brandbox_orderstatus = d['brandbox_orderstatus']
        if 'can_modify_keyword' in d:
            o.can_modify_keyword = d['can_modify_keyword']
        if 'describe' in d:
            o.describe = d['describe']
        if 'detail_base_items' in d:
            o.detail_base_items = d['detail_base_items']
        if 'detail_brand_items' in d:
            o.detail_brand_items = d['detail_brand_items']
        if 'detail_service_items' in d:
            o.detail_service_items = d['detail_service_items']
        if 'final_status' in d:
            o.final_status = d['final_status']
        if 'gmtmodified' in d:
            o.gmtmodified = d['gmtmodified']
        if 'keyword_gmt_modified' in d:
            o.keyword_gmt_modified = d['keyword_gmt_modified']
        if 'online_time' in d:
            o.online_time = d['online_time']
        if 'operator_type' in d:
            o.operator_type = d['operator_type']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'partner_type' in d:
            o.partner_type = d['partner_type']
        if 'reject_node' in d:
            o.reject_node = d['reject_node']
        if 'reject_reason' in d:
            o.reject_reason = d['reject_reason']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'scene_name' in d:
            o.scene_name = d['scene_name']
        if 'service_code' in d:
            o.service_code = d['service_code']
        if 'service_name' in d:
            o.service_name = d['service_name']
        if 'status' in d:
            o.status = d['status']
        if 'sub_service_code' in d:
            o.sub_service_code = d['sub_service_code']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'template_name' in d:
            o.template_name = d['template_name']
        return o


