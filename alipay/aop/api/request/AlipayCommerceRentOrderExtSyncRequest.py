#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.ParamConstants import *

from alipay.aop.api.domain.SellerSyncRentBuyerExtInfo import SellerSyncRentBuyerExtInfo
from alipay.aop.api.domain.SellerSyncRentDeliveryExtInfo import SellerSyncRentDeliveryExtInfo
from alipay.aop.api.domain.SellerSyncRentFinancingExtInfo import SellerSyncRentFinancingExtInfo
from alipay.aop.api.domain.SellerSyncRentItemExtInfo import SellerSyncRentItemExtInfo
from alipay.aop.api.domain.SellerSyncRentOrderExtInfo import SellerSyncRentOrderExtInfo



class AlipayCommerceRentOrderExtSyncRequest(object):

    def __init__(self, biz_model=None):
        self._biz_model = biz_model
        self._buyer_ext_info = None
        self._buyer_id = None
        self._buyer_open_id = None
        self._delivery_ext_info = None
        self._financing_ext_info = None
        self._item_ext_info = None
        self._order_ext_info = None
        self._order_id = None
        self._out_biz_id = None
        self._sync_scene = None
        self._buyer_cert_back_pic = None
        self._buyer_cert_front_pic = None
        self._buyer_live_pic = None
        self._delivery_received_pic = None
        self._financing_rent_protocol = None
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
    def buyer_ext_info(self):
        return self._buyer_ext_info

    @buyer_ext_info.setter
    def buyer_ext_info(self, value):
        if isinstance(value, SellerSyncRentBuyerExtInfo):
            self._buyer_ext_info = value
        else:
            self._buyer_ext_info = SellerSyncRentBuyerExtInfo.from_alipay_dict(value)
    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def buyer_open_id(self):
        return self._buyer_open_id

    @buyer_open_id.setter
    def buyer_open_id(self, value):
        self._buyer_open_id = value
    @property
    def delivery_ext_info(self):
        return self._delivery_ext_info

    @delivery_ext_info.setter
    def delivery_ext_info(self, value):
        if isinstance(value, SellerSyncRentDeliveryExtInfo):
            self._delivery_ext_info = value
        else:
            self._delivery_ext_info = SellerSyncRentDeliveryExtInfo.from_alipay_dict(value)
    @property
    def financing_ext_info(self):
        return self._financing_ext_info

    @financing_ext_info.setter
    def financing_ext_info(self, value):
        if isinstance(value, list):
            self._financing_ext_info = list()
            for i in value:
                if isinstance(i, SellerSyncRentFinancingExtInfo):
                    self._financing_ext_info.append(i)
                else:
                    self._financing_ext_info.append(SellerSyncRentFinancingExtInfo.from_alipay_dict(i))
    @property
    def item_ext_info(self):
        return self._item_ext_info

    @item_ext_info.setter
    def item_ext_info(self, value):
        if isinstance(value, SellerSyncRentItemExtInfo):
            self._item_ext_info = value
        else:
            self._item_ext_info = SellerSyncRentItemExtInfo.from_alipay_dict(value)
    @property
    def order_ext_info(self):
        return self._order_ext_info

    @order_ext_info.setter
    def order_ext_info(self, value):
        if isinstance(value, SellerSyncRentOrderExtInfo):
            self._order_ext_info = value
        else:
            self._order_ext_info = SellerSyncRentOrderExtInfo.from_alipay_dict(value)
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_biz_id(self):
        return self._out_biz_id

    @out_biz_id.setter
    def out_biz_id(self, value):
        self._out_biz_id = value
    @property
    def sync_scene(self):
        return self._sync_scene

    @sync_scene.setter
    def sync_scene(self, value):
        self._sync_scene = value

    @property
    def buyer_cert_back_pic(self):
        return self._buyer_cert_back_pic

    @buyer_cert_back_pic.setter
    def buyer_cert_back_pic(self, value):
        if not isinstance(value, FileItem):
            return
        self._buyer_cert_back_pic = value
    @property
    def buyer_cert_front_pic(self):
        return self._buyer_cert_front_pic

    @buyer_cert_front_pic.setter
    def buyer_cert_front_pic(self, value):
        if not isinstance(value, FileItem):
            return
        self._buyer_cert_front_pic = value
    @property
    def buyer_live_pic(self):
        return self._buyer_live_pic

    @buyer_live_pic.setter
    def buyer_live_pic(self, value):
        if not isinstance(value, FileItem):
            return
        self._buyer_live_pic = value
    @property
    def delivery_received_pic(self):
        return self._delivery_received_pic

    @delivery_received_pic.setter
    def delivery_received_pic(self, value):
        if not isinstance(value, FileItem):
            return
        self._delivery_received_pic = value
    @property
    def financing_rent_protocol(self):
        return self._financing_rent_protocol

    @financing_rent_protocol.setter
    def financing_rent_protocol(self, value):
        if not isinstance(value, FileItem):
            return
        self._financing_rent_protocol = value

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
        params[P_METHOD] = 'alipay.commerce.rent.order.ext.sync'
        params[P_VERSION] = self.version
        if self.biz_model:
            params[P_BIZ_CONTENT] = json.dumps(obj=self.biz_model.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.buyer_ext_info:
            if hasattr(self.buyer_ext_info, 'to_alipay_dict'):
                params['buyer_ext_info'] = json.dumps(obj=self.buyer_ext_info.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['buyer_ext_info'] = self.buyer_ext_info
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = json.dumps(obj=self.buyer_id.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['buyer_id'] = self.buyer_id
        if self.buyer_open_id:
            if hasattr(self.buyer_open_id, 'to_alipay_dict'):
                params['buyer_open_id'] = json.dumps(obj=self.buyer_open_id.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['buyer_open_id'] = self.buyer_open_id
        if self.delivery_ext_info:
            if hasattr(self.delivery_ext_info, 'to_alipay_dict'):
                params['delivery_ext_info'] = json.dumps(obj=self.delivery_ext_info.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['delivery_ext_info'] = self.delivery_ext_info
        if self.financing_ext_info:
            if isinstance(self.financing_ext_info, list):
                for i in range(0, len(self.financing_ext_info)):
                    element = self.financing_ext_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.financing_ext_info[i] = element.to_alipay_dict()
                params['financing_ext_info'] = json.dumps(obj=self.financing_ext_info, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.item_ext_info:
            if hasattr(self.item_ext_info, 'to_alipay_dict'):
                params['item_ext_info'] = json.dumps(obj=self.item_ext_info.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['item_ext_info'] = self.item_ext_info
        if self.order_ext_info:
            if hasattr(self.order_ext_info, 'to_alipay_dict'):
                params['order_ext_info'] = json.dumps(obj=self.order_ext_info.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['order_ext_info'] = self.order_ext_info
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = json.dumps(obj=self.order_id.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['order_id'] = self.order_id
        if self.out_biz_id:
            if hasattr(self.out_biz_id, 'to_alipay_dict'):
                params['out_biz_id'] = json.dumps(obj=self.out_biz_id.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['out_biz_id'] = self.out_biz_id
        if self.sync_scene:
            if hasattr(self.sync_scene, 'to_alipay_dict'):
                params['sync_scene'] = json.dumps(obj=self.sync_scene.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['sync_scene'] = self.sync_scene
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
        if self.buyer_cert_back_pic:
            multipart_params['buyer_cert_back_pic'] = self.buyer_cert_back_pic
        if self.buyer_cert_front_pic:
            multipart_params['buyer_cert_front_pic'] = self.buyer_cert_front_pic
        if self.buyer_live_pic:
            multipart_params['buyer_live_pic'] = self.buyer_live_pic
        if self.delivery_received_pic:
            multipart_params['delivery_received_pic'] = self.delivery_received_pic
        if self.financing_rent_protocol:
            multipart_params['financing_rent_protocol'] = self.financing_rent_protocol
        return multipart_params
