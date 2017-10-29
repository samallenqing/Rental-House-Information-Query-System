package qq.model.service;

import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import qq.model.entity.Ad;

import java.io.IOException;
import java.util.List;


public interface AdService {
    List<Ad> findAdsByLocationOrZip(String zipCodeOrLocation) throws IOException;
}
