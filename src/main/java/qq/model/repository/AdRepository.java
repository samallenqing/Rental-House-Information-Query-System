package qq.model.repository;

import org.springframework.data.repository.CrudRepository;
import org.springframework.data.repository.PagingAndSortingRepository;
import org.springframework.stereotype.Repository;
import qq.model.entity.Ad;

import java.util.List;

@Repository
public interface AdRepository extends CrudRepository<Ad, Long>, PagingAndSortingRepository<Ad,Long> {
    List<Ad> findAdsByZipCode(String zipCode);
    List<Ad> findAdsByLocationContains(String name);
}
